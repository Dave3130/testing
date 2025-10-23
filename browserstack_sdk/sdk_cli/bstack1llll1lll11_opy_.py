# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1lll111ll1l_opy_,
    bstack1lllll11l1l_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
from bstack_utils.constants import EVENTS
class bstack1llllll11ll_opy_(bstack1lll111ll1l_opy_):
    bstack1l1llll1l1l_opy_ = bstack111111l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥᔦ")
    NAME = bstack111111l_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᔧ")
    bstack1llll11ll11_opy_ = bstack111111l_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࠨᔨ")
    bstack1lll1lll1ll_opy_ = bstack111111l_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᔩ")
    bstack11lllll11ll_opy_ = bstack111111l_opy_ (u"ࠢࡪࡰࡳࡹࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᔪ")
    bstack1lll1l1ll11_opy_ = bstack111111l_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᔫ")
    bstack1lll111l1ll_opy_ = bstack111111l_opy_ (u"ࠤ࡬ࡷࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡭ࡻࡢࠣᔬ")
    bstack11lllll1l11_opy_ = bstack111111l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᔭ")
    bstack11lllll1l1l_opy_ = bstack111111l_opy_ (u"ࠦࡪࡴࡤࡦࡦࡢࡥࡹࠨᔮ")
    bstack1llllllll1l_opy_ = bstack111111l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠨᔯ")
    bstack1llll1ll11l_opy_ = bstack111111l_opy_ (u"ࠨ࡮ࡦࡹࡶࡩࡸࡹࡩࡰࡰࠥᔰ")
    bstack11llll1llll_opy_ = bstack111111l_opy_ (u"ࠢࡨࡧࡷࠦᔱ")
    bstack1l11l111111_opy_ = bstack111111l_opy_ (u"ࠣࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧᔲ")
    bstack1l1lll1ll11_opy_ = bstack111111l_opy_ (u"ࠤࡺ࠷ࡨ࡫ࡸࡦࡥࡸࡸࡪࡹࡣࡳ࡫ࡳࡸࠧᔳ")
    bstack1l1llll1111_opy_ = bstack111111l_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࡧࡳࡺࡰࡦࠦᔴ")
    bstack11lllll1111_opy_ = bstack111111l_opy_ (u"ࠦࡶࡻࡩࡵࠤᔵ")
    bstack1l1111l1l11_opy_: Dict[str, List[Callable]] = dict()
    bstack1lllll1111l_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1l1lll_opy_: Any
    bstack1l1lll111ll_opy_: Dict
    def __init__(
        self,
        bstack1lllll1111l_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llll1l1lll_opy_: Dict[str, Any],
        methods=[bstack111111l_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢᔶ"), bstack111111l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᔷ"), bstack111111l_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᔸ"), bstack111111l_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᔹ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1lllll1111l_opy_ = bstack1lllll1111l_opy_
        self.platform_index = platform_index
        self.bstack1l1lll1l111_opy_(methods)
        self.bstack1llll1l1lll_opy_ = bstack1llll1l1lll_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll111ll1l_opy_.get_data(bstack1llllll11ll_opy_.bstack1lll1lll1ll_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll111ll1l_opy_.get_data(bstack1llllll11ll_opy_.bstack1llll11ll11_opy_, target, strict)
    @staticmethod
    def bstack11lllll111l_opy_(target: object, strict=True):
        return bstack1lll111ll1l_opy_.get_data(bstack1llllll11ll_opy_.bstack11lllll11ll_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll111ll1l_opy_.get_data(bstack1llllll11ll_opy_.bstack1lll1l1ll11_opy_, target, strict)
    @staticmethod
    def bstack1lll11lll1l_opy_(instance: bstack1lllll11l1l_opy_) -> bool:
        return bstack1lll111ll1l_opy_.get_state(instance, bstack1llllll11ll_opy_.bstack1lll111l1ll_opy_, False)
    @staticmethod
    def bstack1l1llll11ll_opy_(instance: bstack1lllll11l1l_opy_, default_value=None):
        return bstack1lll111ll1l_opy_.get_state(instance, bstack1llllll11ll_opy_.bstack1llll11ll11_opy_, default_value)
    @staticmethod
    def bstack1l1lll11l1l_opy_(instance: bstack1lllll11l1l_opy_, default_value=None):
        return bstack1lll111ll1l_opy_.get_state(instance, bstack1llllll11ll_opy_.bstack1lll1l1ll11_opy_, default_value)
    @staticmethod
    def bstack1lll111l11l_opy_(hub_url: str, bstack11lllll1ll1_opy_=bstack111111l_opy_ (u"ࠤ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࠨᔺ")):
        try:
            bstack11lllll11l1_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11lllll11l1_opy_.endswith(bstack11lllll1ll1_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll111l1_opy_(method_name: str):
        return method_name == bstack111111l_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᔻ")
    @staticmethod
    def bstack1llllllllll_opy_(method_name: str, *args):
        return (
            bstack1llllll11ll_opy_.bstack1l1lll111l1_opy_(method_name)
            and bstack1llllll11ll_opy_.bstack1111111111_opy_(*args) == bstack1llllll11ll_opy_.bstack1llll1ll11l_opy_
        )
    @staticmethod
    def bstack1l1lll1l1ll_opy_(method_name: str, *args):
        if not bstack1llllll11ll_opy_.bstack1l1lll111l1_opy_(method_name):
            return False
        if not bstack1llllll11ll_opy_.bstack1l1lll1ll11_opy_ in bstack1llllll11ll_opy_.bstack1111111111_opy_(*args):
            return False
        bstack1l1lll1l11l_opy_ = bstack1llllll11ll_opy_.bstack1l1lll1ll1l_opy_(*args)
        return bstack1l1lll1l11l_opy_ and bstack111111l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᔼ") in bstack1l1lll1l11l_opy_ and bstack111111l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᔽ") in bstack1l1lll1l11l_opy_[bstack111111l_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᔾ")]
    @staticmethod
    def bstack1l1llll1l11_opy_(method_name: str, *args):
        if not bstack1llllll11ll_opy_.bstack1l1lll111l1_opy_(method_name):
            return False
        if not bstack1llllll11ll_opy_.bstack1l1lll1ll11_opy_ in bstack1llllll11ll_opy_.bstack1111111111_opy_(*args):
            return False
        bstack1l1lll1l11l_opy_ = bstack1llllll11ll_opy_.bstack1l1lll1ll1l_opy_(*args)
        return (
            bstack1l1lll1l11l_opy_
            and bstack111111l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᔿ") in bstack1l1lll1l11l_opy_
            and bstack111111l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸࡩࡲࡪࡲࡷࠦᕀ") in bstack1l1lll1l11l_opy_[bstack111111l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕁ")]
        )
    @staticmethod
    def bstack1111111111_opy_(*args):
        return str(bstack1llllll11ll_opy_.bstack1l1llll11l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1llll11l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1ll1l_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11l1l11ll1_opy_(driver):
        command_executor = getattr(driver, bstack111111l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᕂ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack111111l_opy_ (u"ࠦࡤࡻࡲ࡭ࠤᕃ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack111111l_opy_ (u"ࠧࡥࡣ࡭࡫ࡨࡲࡹࡥࡣࡰࡰࡩ࡭࡬ࠨᕄ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack111111l_opy_ (u"ࠨࡲࡦ࡯ࡲࡸࡪࡥࡳࡦࡴࡹࡩࡷࡥࡡࡥࡦࡵࠦᕅ"), None)
        return hub_url
    def bstack1lllll1l11l_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack111111l_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕆ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack111111l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕇ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack111111l_opy_ (u"ࠤࡢࡹࡷࡲࠢᕈ")):
                setattr(command_executor, bstack111111l_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᕉ"), hub_url)
                result = True
        if result:
            self.bstack1lllll1111l_opy_ = hub_url
            bstack1llllll11ll_opy_.bstack1llll1lll1l_opy_(instance, bstack1llllll11ll_opy_.bstack1llll11ll11_opy_, hub_url)
            bstack1llllll11ll_opy_.bstack1llll1lll1l_opy_(
                instance, bstack1llllll11ll_opy_.bstack1lll111l1ll_opy_, bstack1llllll11ll_opy_.bstack1lll111l11l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll11lll_opy_(bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_]):
        return bstack111111l_opy_ (u"ࠦ࠿ࠨᕊ").join((bstack1llll1lllll_opy_(bstack1lllll1l1ll_opy_[0]).name, bstack1llll1ll111_opy_(bstack1lllll1l1ll_opy_[1]).name))
    @staticmethod
    def bstack1111111l11_opy_(bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_], callback: Callable):
        bstack1l1lll1l1l1_opy_ = bstack1llllll11ll_opy_.bstack1l1lll11lll_opy_(bstack1lllll1l1ll_opy_)
        if not bstack1l1lll1l1l1_opy_ in bstack1llllll11ll_opy_.bstack1l1111l1l11_opy_:
            bstack1llllll11ll_opy_.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_] = []
        bstack1llllll11ll_opy_.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_].append(callback)
    def bstack1l1lll11l11_opy_(self, instance: bstack1lllll11l1l_opy_, method_name: str, bstack1l1lll1111l_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack111111l_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᕋ")):
            return
        cmd = args[0] if method_name == bstack111111l_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᕌ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1lll1_opy_ = bstack111111l_opy_ (u"ࠢ࠻ࠤᕍ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠤᕎ") + bstack11llll1lll1_opy_, bstack1l1lll1111l_opy_)
    def bstack1l1llll111l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll11111_opy_, bstack1l1lll1lll1_opy_ = bstack1lllll1l1ll_opy_
        bstack1l1lll1l1l1_opy_ = bstack1llllll11ll_opy_.bstack1l1lll11lll_opy_(bstack1lllll1l1ll_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠤࡲࡲࡤ࡮࡯ࡰ࡭࠽ࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᕏ") + str(kwargs) + bstack111111l_opy_ (u"ࠥࠦᕐ"))
        if bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.QUIT:
            if bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.PRE:
                bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack1ll1lll11_opy_.value)
                bstack1lll111ll1l_opy_.bstack1llll1lll1l_opy_(instance, EVENTS.bstack1ll1lll11_opy_.value, bstack1ll1l1ll1ll_opy_)
                self.logger.debug(bstack111111l_opy_ (u"ࠦ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠡࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁࡽࠣᕑ").format(instance, method_name, bstack1l1lll11111_opy_, bstack1l1lll1lll1_opy_))
        if bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.bstack111111l111_opy_:
            if bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.POST and not bstack1llllll11ll_opy_.bstack1lll1lll1ll_opy_ in instance.data:
                session_id = getattr(target, bstack111111l_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᕒ"), None)
                if session_id:
                    instance.data[bstack1llllll11ll_opy_.bstack1lll1lll1ll_opy_] = session_id
        elif (
            bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.bstack11111111l1_opy_
            and bstack1llllll11ll_opy_.bstack1111111111_opy_(*args) == bstack1llllll11ll_opy_.bstack1llll1ll11l_opy_
        ):
            if bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.PRE:
                hub_url = bstack1llllll11ll_opy_.bstack11l1l11ll1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1llllll11ll_opy_.bstack1llll11ll11_opy_: hub_url,
                            bstack1llllll11ll_opy_.bstack1lll111l1ll_opy_: bstack1llllll11ll_opy_.bstack1lll111l11l_opy_(hub_url),
                            bstack1llllll11ll_opy_.bstack1llllllll1l_opy_: int(
                                os.environ.get(bstack111111l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᕓ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll1l11l_opy_ = bstack1llllll11ll_opy_.bstack1l1lll1ll1l_opy_(*args)
                bstack11lllll111l_opy_ = bstack1l1lll1l11l_opy_.get(bstack111111l_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᕔ"), None) if bstack1l1lll1l11l_opy_ else None
                if isinstance(bstack11lllll111l_opy_, dict):
                    instance.data[bstack1llllll11ll_opy_.bstack11lllll11ll_opy_] = copy.deepcopy(bstack11lllll111l_opy_)
                    instance.data[bstack1llllll11ll_opy_.bstack1lll1l1ll11_opy_] = bstack11lllll111l_opy_
            elif bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack111111l_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢᕕ"), dict()).get(bstack111111l_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡌࡨࠧᕖ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1llllll11ll_opy_.bstack1lll1lll1ll_opy_: framework_session_id,
                                bstack1llllll11ll_opy_.bstack11lllll1l11_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.bstack11111111l1_opy_
            and bstack1llllll11ll_opy_.bstack1111111111_opy_(*args) == bstack1llllll11ll_opy_.bstack11lllll1111_opy_
            and bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.POST
        ):
            instance.data[bstack1llllll11ll_opy_.bstack11lllll1l1l_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll1l1l1_opy_ in bstack1llllll11ll_opy_.bstack1l1111l1l11_opy_:
            bstack1l1ll1lllll_opy_ = None
            for callback in bstack1llllll11ll_opy_.bstack1l1111l1l11_opy_[bstack1l1lll1l1l1_opy_]:
                try:
                    bstack1l1lll11ll1_opy_ = callback(self, target, exec, bstack1lllll1l1ll_opy_, result, *args, **kwargs)
                    if bstack1l1ll1lllll_opy_ == None:
                        bstack1l1ll1lllll_opy_ = bstack1l1lll11ll1_opy_
                except Exception as e:
                    self.logger.error(bstack111111l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢ࡬ࡲࡻࡵ࡫ࡪࡰࡪࠤࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࠣᕗ") + str(e) + bstack111111l_opy_ (u"ࠦࠧᕘ"))
                    traceback.print_exc()
            if bstack1l1lll11111_opy_ == bstack1llll1lllll_opy_.QUIT:
                if bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.POST:
                    bstack1ll1l1ll1ll_opy_ = bstack1lll111ll1l_opy_.get_state(instance, EVENTS.bstack1ll1lll11_opy_.value)
                    if bstack1ll1l1ll1ll_opy_!=None:
                        bstack1llllll1lll_opy_.end(EVENTS.bstack1ll1lll11_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᕙ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᕚ"), True, None)
            if bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.PRE and callable(bstack1l1ll1lllll_opy_):
                return bstack1l1ll1lllll_opy_
            elif bstack1l1lll1lll1_opy_ == bstack1llll1ll111_opy_.POST and bstack1l1ll1lllll_opy_:
                return bstack1l1ll1lllll_opy_
    def bstack1l1ll1llll1_opy_(
        self, method_name, previous_state: bstack1llll1lllll_opy_, *args, **kwargs
    ) -> bstack1llll1lllll_opy_:
        if method_name == bstack111111l_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤᕛ") or method_name == bstack111111l_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣᕜ"):
            return bstack1llll1lllll_opy_.bstack111111l111_opy_
        if method_name == bstack111111l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᕝ"):
            return bstack1llll1lllll_opy_.QUIT
        if method_name == bstack111111l_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᕞ"):
            if previous_state != bstack1llll1lllll_opy_.NONE:
                command_name = bstack1llllll11ll_opy_.bstack1111111111_opy_(*args)
                if command_name == bstack1llllll11ll_opy_.bstack1llll1ll11l_opy_:
                    return bstack1llll1lllll_opy_.bstack111111l111_opy_
            return bstack1llll1lllll_opy_.bstack11111111l1_opy_
        return bstack1llll1lllll_opy_.NONE