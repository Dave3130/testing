# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l11l1lll_opy_ import get_logger
from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
bstack1l11l1l11_opy_ = bstack1llllll11ll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11l1111ll1_opy_: Optional[str] = None):
    bstack111l1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡊࡥࡤࡱࡵࡥࡹࡵࡲࠡࡶࡲࠤࡱࡵࡧࠡࡶ࡫ࡩࠥࡹࡴࡢࡴࡷࠤࡹ࡯࡭ࡦࠢࡲࡪࠥࡧࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࡤࡰࡴࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࠥࡴࡡ࡮ࡧࠣࡥࡳࡪࠠࡴࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢ᚛")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11l11lll_opy_: str = bstack1l11l1l11_opy_.bstack11ll1l11ll1_opy_(label)
            start_mark: str = label + bstack111l1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ᚜")
            end_mark: str = label + bstack111l1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ᚝")
            result = None
            try:
                if stage.value == STAGE.bstack11ll1l111l_opy_.value:
                    bstack1l11l1l11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1l11l1l11_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11l1111ll1_opy_)
                elif stage.value == STAGE.bstack1ll1ll111_opy_.value:
                    start_mark: str = bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ᚞")
                    end_mark: str = bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ᚟")
                    bstack1l11l1l11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1l11l1l11_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11l1111ll1_opy_)
            except Exception as e:
                bstack1l11l1l11_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11l1111ll1_opy_)
            return result
        return wrapper
    return decorator