# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import (
    bstack1lll111llll_opy_,
    bstack111111l111_opy_,
    bstack1111111l11_opy_,
    bstack1llllll1ll1_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll1ll1l_opy_(bstack1lll111llll_opy_):
    bstack1l1lll111l1_opy_ = bstack1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᔳ")
    NAME = bstack1l_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧᔴ")
    bstack1llll111ll1_opy_ = bstack1l_opy_ (u"ࠦ࡭ࡻࡢࡠࡷࡵࡰࠧᔵ")
    bstack1llll11lll1_opy_ = bstack1l_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᔶ")
    bstack11lllll1l11_opy_ = bstack1l_opy_ (u"ࠨࡩ࡯ࡲࡸࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᔷ")
    bstack1lll1llllll_opy_ = bstack1l_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᔸ")
    bstack1lll11l111l_opy_ = bstack1l_opy_ (u"ࠣ࡫ࡶࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡬ࡺࡨࠢᔹ")
    bstack11lllll11l1_opy_ = bstack1l_opy_ (u"ࠤࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᔺ")
    bstack11lllll1ll1_opy_ = bstack1l_opy_ (u"ࠥࡩࡳࡪࡥࡥࡡࡤࡸࠧᔻ")
    bstack1llll1lllll_opy_ = bstack1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠧᔼ")
    bstack1llllllll1l_opy_ = bstack1l_opy_ (u"ࠧࡴࡥࡸࡵࡨࡷࡸ࡯࡯࡯ࠤᔽ")
    bstack11lllll1l1l_opy_ = bstack1l_opy_ (u"ࠨࡧࡦࡶࠥᔾ")
    bstack1l11ll11ll1_opy_ = bstack1l_opy_ (u"ࠢࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠦᔿ")
    bstack1l1llll11ll_opy_ = bstack1l_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࠦᕀ")
    bstack1l1lll11l11_opy_ = bstack1l_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࡦࡹࡹ࡯ࡥࠥᕁ")
    bstack11llllll111_opy_ = bstack1l_opy_ (u"ࠥࡵࡺ࡯ࡴࠣᕂ")
    bstack1l1111l11l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1lllll1l1l1_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll1lll1_opy_: Any
    bstack1l1llll1l1l_opy_: Dict
    def __init__(
        self,
        bstack1lllll1l1l1_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lllll1lll1_opy_: Dict[str, Any],
        methods=[bstack1l_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨᕃ"), bstack1l_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᕄ"), bstack1l_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᕅ"), bstack1l_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᕆ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1lllll1l1l1_opy_ = bstack1lllll1l1l1_opy_
        self.platform_index = platform_index
        self.bstack1l1lll1l111_opy_(methods)
        self.bstack1lllll1lll1_opy_ = bstack1lllll1lll1_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll111llll_opy_.get_data(bstack1lllll1ll1l_opy_.bstack1llll11lll1_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll111llll_opy_.get_data(bstack1lllll1ll1l_opy_.bstack1llll111ll1_opy_, target, strict)
    @staticmethod
    def bstack11lllll1111_opy_(target: object, strict=True):
        return bstack1lll111llll_opy_.get_data(bstack1lllll1ll1l_opy_.bstack11lllll1l11_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll111llll_opy_.get_data(bstack1lllll1ll1l_opy_.bstack1lll1llllll_opy_, target, strict)
    @staticmethod
    def bstack1lll11lll11_opy_(instance: bstack111111l111_opy_) -> bool:
        return bstack1lll111llll_opy_.get_state(instance, bstack1lllll1ll1l_opy_.bstack1lll11l111l_opy_, False)
    @staticmethod
    def bstack1l1llll1ll1_opy_(instance: bstack111111l111_opy_, default_value=None):
        return bstack1lll111llll_opy_.get_state(instance, bstack1lllll1ll1l_opy_.bstack1llll111ll1_opy_, default_value)
    @staticmethod
    def bstack1l1lll1l1ll_opy_(instance: bstack111111l111_opy_, default_value=None):
        return bstack1lll111llll_opy_.get_state(instance, bstack1lllll1ll1l_opy_.bstack1lll1llllll_opy_, default_value)
    @staticmethod
    def bstack1lll1111lll_opy_(hub_url: str, bstack11lllll11ll_opy_=bstack1l_opy_ (u"ࠣ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧᕇ")):
        try:
            bstack11lllll111l_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11lllll111l_opy_.endswith(bstack11lllll11ll_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll11lll_opy_(method_name: str):
        return method_name == bstack1l_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕈ")
    @staticmethod
    def bstack1lllll1llll_opy_(method_name: str, *args):
        return (
            bstack1lllll1ll1l_opy_.bstack1l1lll11lll_opy_(method_name)
            and bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args) == bstack1lllll1ll1l_opy_.bstack1llllllll1l_opy_
        )
    @staticmethod
    def bstack1l1llll111l_opy_(method_name: str, *args):
        if not bstack1lllll1ll1l_opy_.bstack1l1lll11lll_opy_(method_name):
            return False
        if not bstack1lllll1ll1l_opy_.bstack1l1llll11ll_opy_ in bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll11111_opy_ = bstack1lllll1ll1l_opy_.bstack1l1lll1ll11_opy_(*args)
        return bstack1l1lll11111_opy_ and bstack1l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕉ") in bstack1l1lll11111_opy_ and bstack1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᕊ") in bstack1l1lll11111_opy_[bstack1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕋ")]
    @staticmethod
    def bstack1l1lll1111l_opy_(method_name: str, *args):
        if not bstack1lllll1ll1l_opy_.bstack1l1lll11lll_opy_(method_name):
            return False
        if not bstack1lllll1ll1l_opy_.bstack1l1llll11ll_opy_ in bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll11111_opy_ = bstack1lllll1ll1l_opy_.bstack1l1lll1ll11_opy_(*args)
        return (
            bstack1l1lll11111_opy_
            and bstack1l_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᕌ") in bstack1l1lll11111_opy_
            and bstack1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡨࡸࡩࡱࡶࠥᕍ") in bstack1l1lll11111_opy_[bstack1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕎ")]
        )
    @staticmethod
    def bstack1llllll111l_opy_(*args):
        return str(bstack1lllll1ll1l_opy_.bstack1l1llll11l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1llll11l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1ll11_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11l1l11ll1_opy_(driver):
        command_executor = getattr(driver, bstack1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᕏ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1l_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᕐ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1l_opy_ (u"ࠦࡤࡩ࡬ࡪࡧࡱࡸࡤࡩ࡯࡯ࡨ࡬࡫ࠧᕑ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1l_opy_ (u"ࠧࡸࡥ࡮ࡱࡷࡩࡤࡹࡥࡳࡸࡨࡶࡤࡧࡤࡥࡴࠥᕒ"), None)
        return hub_url
    def bstack1lllll11l11_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕓ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕔ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1l_opy_ (u"ࠣࡡࡸࡶࡱࠨᕕ")):
                setattr(command_executor, bstack1l_opy_ (u"ࠤࡢࡹࡷࡲࠢᕖ"), hub_url)
                result = True
        if result:
            self.bstack1lllll1l1l1_opy_ = hub_url
            bstack1lllll1ll1l_opy_.bstack1lllll11ll1_opy_(instance, bstack1lllll1ll1l_opy_.bstack1llll111ll1_opy_, hub_url)
            bstack1lllll1ll1l_opy_.bstack1lllll11ll1_opy_(
                instance, bstack1lllll1ll1l_opy_.bstack1lll11l111l_opy_, bstack1lllll1ll1l_opy_.bstack1lll1111lll_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_]):
        return bstack1l_opy_ (u"ࠥ࠾ࠧᕗ").join((bstack1111111l11_opy_(bstack1lllll1ll11_opy_[0]).name, bstack1llllll1ll1_opy_(bstack1lllll1ll11_opy_[1]).name))
    @staticmethod
    def bstack1lllll1111l_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_], callback: Callable):
        bstack1l1llll1111_opy_ = bstack1lllll1ll1l_opy_.bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_)
        if not bstack1l1llll1111_opy_ in bstack1lllll1ll1l_opy_.bstack1l1111l11l1_opy_:
            bstack1lllll1ll1l_opy_.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_] = []
        bstack1lllll1ll1l_opy_.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_].append(callback)
    def bstack1l1ll1lllll_opy_(self, instance: bstack111111l111_opy_, method_name: str, bstack1l1lll1l1l1_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᕘ")):
            return
        cmd = args[0] if method_name == bstack1l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᕙ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11lllll1lll_opy_ = bstack1l_opy_ (u"ࠨ࠺ࠣᕚ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠣᕛ") + bstack11lllll1lll_opy_, bstack1l1lll1l1l1_opy_)
    def bstack1l1lll1ll1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack111111l111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1111111l11_opy_, bstack1llllll1ll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll1lll1_opy_, bstack1l1lll1l11l_opy_ = bstack1lllll1ll11_opy_
        bstack1l1llll1111_opy_ = bstack1lllll1ll1l_opy_.bstack1l1lll11ll1_opy_(bstack1lllll1ll11_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠣࡱࡱࡣ࡭ࡵ࡯࡬࠼ࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫ࡽࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᕜ") + str(kwargs) + bstack1l_opy_ (u"ࠤࠥᕝ"))
        if bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.QUIT:
            if bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.PRE:
                bstack1ll1l1lll11_opy_ = bstack1llll1l1lll_opy_.bstack1ll11llllll_opy_(EVENTS.bstack1l1ll1l111_opy_.value)
                bstack1lll111llll_opy_.bstack1lllll11ll1_opy_(instance, EVENTS.bstack1l1ll1l111_opy_.value, bstack1ll1l1lll11_opy_)
                self.logger.debug(bstack1l_opy_ (u"ࠥ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࢁࡽࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠠࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࢃࠢᕞ").format(instance, method_name, bstack1l1lll1lll1_opy_, bstack1l1lll1l11l_opy_))
        if bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.bstack1llllll1l1l_opy_:
            if bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.POST and not bstack1lllll1ll1l_opy_.bstack1llll11lll1_opy_ in instance.data:
                session_id = getattr(target, bstack1l_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣᕟ"), None)
                if session_id:
                    instance.data[bstack1lllll1ll1l_opy_.bstack1llll11lll1_opy_] = session_id
        elif (
            bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.bstack1111111ll1_opy_
            and bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args) == bstack1lllll1ll1l_opy_.bstack1llllllll1l_opy_
        ):
            if bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.PRE:
                hub_url = bstack1lllll1ll1l_opy_.bstack11l1l11ll1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll1ll1l_opy_.bstack1llll111ll1_opy_: hub_url,
                            bstack1lllll1ll1l_opy_.bstack1lll11l111l_opy_: bstack1lllll1ll1l_opy_.bstack1lll1111lll_opy_(hub_url),
                            bstack1lllll1ll1l_opy_.bstack1llll1lllll_opy_: int(
                                os.environ.get(bstack1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧᕠ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll11111_opy_ = bstack1lllll1ll1l_opy_.bstack1l1lll1ll11_opy_(*args)
                bstack11lllll1111_opy_ = bstack1l1lll11111_opy_.get(bstack1l_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᕡ"), None) if bstack1l1lll11111_opy_ else None
                if isinstance(bstack11lllll1111_opy_, dict):
                    instance.data[bstack1lllll1ll1l_opy_.bstack11lllll1l11_opy_] = copy.deepcopy(bstack11lllll1111_opy_)
                    instance.data[bstack1lllll1ll1l_opy_.bstack1lll1llllll_opy_] = bstack11lllll1111_opy_
            elif bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1l_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࠨᕢ"), dict()).get(bstack1l_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡋࡧࠦᕣ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll1ll1l_opy_.bstack1llll11lll1_opy_: framework_session_id,
                                bstack1lllll1ll1l_opy_.bstack11lllll11l1_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.bstack1111111ll1_opy_
            and bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args) == bstack1lllll1ll1l_opy_.bstack11llllll111_opy_
            and bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.POST
        ):
            instance.data[bstack1lllll1ll1l_opy_.bstack11lllll1ll1_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1llll1111_opy_ in bstack1lllll1ll1l_opy_.bstack1l1111l11l1_opy_:
            bstack1l1llll1l11_opy_ = None
            for callback in bstack1lllll1ll1l_opy_.bstack1l1111l11l1_opy_[bstack1l1llll1111_opy_]:
                try:
                    bstack1l1lll11l1l_opy_ = callback(self, target, exec, bstack1lllll1ll11_opy_, result, *args, **kwargs)
                    if bstack1l1llll1l11_opy_ == None:
                        bstack1l1llll1l11_opy_ = bstack1l1lll11l1l_opy_
                except Exception as e:
                    self.logger.error(bstack1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠡ࡫ࡱࡺࡴࡱࡩ࡯ࡩࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࠢᕤ") + str(e) + bstack1l_opy_ (u"ࠥࠦᕥ"))
                    traceback.print_exc()
            if bstack1l1lll1lll1_opy_ == bstack1111111l11_opy_.QUIT:
                if bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.POST:
                    bstack1ll1l1lll11_opy_ = bstack1lll111llll_opy_.get_state(instance, EVENTS.bstack1l1ll1l111_opy_.value)
                    if bstack1ll1l1lll11_opy_!=None:
                        bstack1llll1l1lll_opy_.end(EVENTS.bstack1l1ll1l111_opy_.value, bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᕦ"), bstack1ll1l1lll11_opy_+bstack1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᕧ"), True, None)
            if bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.PRE and callable(bstack1l1llll1l11_opy_):
                return bstack1l1llll1l11_opy_
            elif bstack1l1lll1l11l_opy_ == bstack1llllll1ll1_opy_.POST and bstack1l1llll1l11_opy_:
                return bstack1l1llll1l11_opy_
    def bstack1l1lll111ll_opy_(
        self, method_name, previous_state: bstack1111111l11_opy_, *args, **kwargs
    ) -> bstack1111111l11_opy_:
        if method_name == bstack1l_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣᕨ") or method_name == bstack1l_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᕩ"):
            return bstack1111111l11_opy_.bstack1llllll1l1l_opy_
        if method_name == bstack1l_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᕪ"):
            return bstack1111111l11_opy_.QUIT
        if method_name == bstack1l_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕫ"):
            if previous_state != bstack1111111l11_opy_.NONE:
                command_name = bstack1lllll1ll1l_opy_.bstack1llllll111l_opy_(*args)
                if command_name == bstack1lllll1ll1l_opy_.bstack1llllllll1l_opy_:
                    return bstack1111111l11_opy_.bstack1llllll1l1l_opy_
            return bstack1111111l11_opy_.bstack1111111ll1_opy_
        return bstack1111111l11_opy_.NONE