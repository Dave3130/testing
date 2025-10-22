# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11ll1ll1l_opy_ import get_logger
from bstack_utils.bstack111llll1l_opy_ import bstack1llll11l1ll_opy_
bstack111llll1l_opy_ = bstack1llll11l1ll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11ll11l111_opy_: Optional[str] = None):
    bstack1l111ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡊࡥࡤࡱࡵࡥࡹࡵࡲࠡࡶࡲࠤࡱࡵࡧࠡࡶ࡫ࡩࠥࡹࡴࡢࡴࡷࠤࡹ࡯࡭ࡦࠢࡲࡪࠥࡧࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࡤࡰࡴࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࠥࡴࡡ࡮ࡧࠣࡥࡳࡪࠠࡴࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢ᚛")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll111ll111_opy_: str = bstack111llll1l_opy_.bstack11ll1l11ll1_opy_(label)
            start_mark: str = label + bstack1l111ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ᚜")
            end_mark: str = label + bstack1l111ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ᚝")
            result = None
            try:
                if stage.value == STAGE.bstack1111l11lll_opy_.value:
                    bstack111llll1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111llll1l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11ll11l111_opy_)
                elif stage.value == STAGE.bstack1ll11l111l_opy_.value:
                    start_mark: str = bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ᚞")
                    end_mark: str = bstack1ll111ll111_opy_ + bstack1l111ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ᚟")
                    bstack111llll1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111llll1l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11ll11l111_opy_)
            except Exception as e:
                bstack111llll1l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11ll11l111_opy_)
            return result
        return wrapper
    return decorator