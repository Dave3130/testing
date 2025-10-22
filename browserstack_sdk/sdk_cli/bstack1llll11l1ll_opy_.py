# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lll1111l1l_opy_,
    bstack1lllll111l1_opy_,
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
from bstack_utils.constants import EVENTS
class bstack1llll1lllll_opy_(bstack1lll1111l1l_opy_):
    bstack1l1lll1l111_opy_ = bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᕑ")
    NAME = bstack1lllll1l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᕒ")
    bstack1lll1lllll1_opy_ = bstack1lllll1l_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲࠢᕓ")
    bstack1lll1llll1l_opy_ = bstack1lllll1l_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᕔ")
    bstack11llll1ll11_opy_ = bstack1lllll1l_opy_ (u"ࠣ࡫ࡱࡴࡺࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᕕ")
    bstack1llll111l11_opy_ = bstack1lllll1l_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᕖ")
    bstack1lll111l111_opy_ = bstack1lllll1l_opy_ (u"ࠥ࡭ࡸࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡮ࡵࡣࠤᕗ")
    bstack11llll1l1l1_opy_ = bstack1lllll1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᕘ")
    bstack11llll1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠧ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᕙ")
    bstack1llllllllll_opy_ = bstack1lllll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᕚ")
    bstack1llllll11ll_opy_ = bstack1lllll1l_opy_ (u"ࠢ࡯ࡧࡺࡷࡪࡹࡳࡪࡱࡱࠦᕛ")
    bstack11llll11l1l_opy_ = bstack1lllll1l_opy_ (u"ࠣࡩࡨࡸࠧᕜ")
    bstack1l11ll111l1_opy_ = bstack1lllll1l_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᕝ")
    bstack1l1ll1l1l11_opy_ = bstack1lllll1l_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࠨᕞ")
    bstack1l1ll1l1lll_opy_ = bstack1lllll1l_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࡡࡴࡻࡱࡧࠧᕟ")
    bstack11llll11lll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡷࡵࡪࡶࠥᕠ")
    bstack1l111111lll_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll1l111l_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1ll11l_opy_: Any
    bstack1l1lll1l1l1_opy_: Dict
    def __init__(
        self,
        bstack1llll1l111l_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llll1ll11l_opy_: Dict[str, Any],
        methods=[bstack1lllll1l_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣᕡ"), bstack1lllll1l_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᕢ"), bstack1lllll1l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕣ"), bstack1lllll1l_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᕤ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llll1l111l_opy_ = bstack1llll1l111l_opy_
        self.platform_index = platform_index
        self.bstack1l1lll11lll_opy_(methods)
        self.bstack1llll1ll11l_opy_ = bstack1llll1ll11l_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll1lllll_opy_.bstack1lll1llll1l_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll1lllll_opy_.bstack1lll1lllll1_opy_, target, strict)
    @staticmethod
    def bstack11llll1l11l_opy_(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll1lllll_opy_.bstack11llll1ll11_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll1lllll_opy_.bstack1llll111l11_opy_, target, strict)
    @staticmethod
    def bstack1lll1111lll_opy_(instance: bstack1lllll111l1_opy_) -> bool:
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll1lllll_opy_.bstack1lll111l111_opy_, False)
    @staticmethod
    def bstack1l1ll1llll1_opy_(instance: bstack1lllll111l1_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll1lllll_opy_.bstack1lll1lllll1_opy_, default_value)
    @staticmethod
    def bstack1l1ll1lllll_opy_(instance: bstack1lllll111l1_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll1lllll_opy_.bstack1llll111l11_opy_, default_value)
    @staticmethod
    def bstack1lll1111111_opy_(hub_url: str, bstack11llll11ll1_opy_=bstack1lllll1l_opy_ (u"ࠥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢᕥ")):
        try:
            bstack11llll1l1ll_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll1l1ll_opy_.endswith(bstack11llll11ll1_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll11l11_opy_(method_name: str):
        return method_name == bstack1lllll1l_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕦ")
    @staticmethod
    def bstack1llll1l1ll1_opy_(method_name: str, *args):
        return (
            bstack1llll1lllll_opy_.bstack1l1lll11l11_opy_(method_name)
            and bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args) == bstack1llll1lllll_opy_.bstack1llllll11ll_opy_
        )
    @staticmethod
    def bstack1l1ll1lll1l_opy_(method_name: str, *args):
        if not bstack1llll1lllll_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1llll1lllll_opy_.bstack1l1ll1l1l11_opy_ in bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args):
            return False
        bstack1l1ll1l1ll1_opy_ = bstack1llll1lllll_opy_.bstack1l1lll1111l_opy_(*args)
        return bstack1l1ll1l1ll1_opy_ and bstack1lllll1l_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕧ") in bstack1l1ll1l1ll1_opy_ and bstack1lllll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᕨ") in bstack1l1ll1l1ll1_opy_[bstack1lllll1l_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕩ")]
    @staticmethod
    def bstack1l1lll111ll_opy_(method_name: str, *args):
        if not bstack1llll1lllll_opy_.bstack1l1lll11l11_opy_(method_name):
            return False
        if not bstack1llll1lllll_opy_.bstack1l1ll1l1l11_opy_ in bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args):
            return False
        bstack1l1ll1l1ll1_opy_ = bstack1llll1lllll_opy_.bstack1l1lll1111l_opy_(*args)
        return (
            bstack1l1ll1l1ll1_opy_
            and bstack1lllll1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕪ") in bstack1l1ll1l1ll1_opy_
            and bstack1lllll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡣࡳ࡫ࡳࡸࠧᕫ") in bstack1l1ll1l1ll1_opy_[bstack1lllll1l_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕬ")]
        )
    @staticmethod
    def bstack1llllllll11_opy_(*args):
        return str(bstack1llll1lllll_opy_.bstack1l1ll1ll1l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1111l_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11l1l11lll_opy_(driver):
        command_executor = getattr(driver, bstack1lllll1l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᕭ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1lllll1l_opy_ (u"ࠧࡥࡵࡳ࡮ࠥᕮ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1lllll1l_opy_ (u"ࠨ࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠢᕯ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1lllll1l_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫࡟ࡴࡧࡵࡺࡪࡸ࡟ࡢࡦࡧࡶࠧᕰ"), None)
        return hub_url
    def bstack1llll11llll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1lllll1l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕱ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1lllll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᕲ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1lllll1l_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᕳ")):
                setattr(command_executor, bstack1lllll1l_opy_ (u"ࠦࡤࡻࡲ࡭ࠤᕴ"), hub_url)
                result = True
        if result:
            self.bstack1llll1l111l_opy_ = hub_url
            bstack1llll1lllll_opy_.bstack1llll11ll1l_opy_(instance, bstack1llll1lllll_opy_.bstack1lll1lllll1_opy_, hub_url)
            bstack1llll1lllll_opy_.bstack1llll11ll1l_opy_(
                instance, bstack1llll1lllll_opy_.bstack1lll111l111_opy_, bstack1llll1lllll_opy_.bstack1lll1111111_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_]):
        return bstack1lllll1l_opy_ (u"ࠧࡀࠢᕵ").join((bstack1lllllll1l1_opy_(bstack1llll1l1lll_opy_[0]).name, bstack1llllll1l11_opy_(bstack1llll1l1lll_opy_[1]).name))
    @staticmethod
    def bstack1llll1l1l11_opy_(bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_], callback: Callable):
        bstack1l1lll1l1ll_opy_ = bstack1llll1lllll_opy_.bstack1l1lll11ll1_opy_(bstack1llll1l1lll_opy_)
        if not bstack1l1lll1l1ll_opy_ in bstack1llll1lllll_opy_.bstack1l111111lll_opy_:
            bstack1llll1lllll_opy_.bstack1l111111lll_opy_[bstack1l1lll1l1ll_opy_] = []
        bstack1llll1lllll_opy_.bstack1l111111lll_opy_[bstack1l1lll1l1ll_opy_].append(callback)
    def bstack1l1ll1l1l1l_opy_(self, instance: bstack1lllll111l1_opy_, method_name: str, bstack1l1ll1ll1ll_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1lllll1l_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᕶ")):
            return
        cmd = args[0] if method_name == bstack1lllll1l_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᕷ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1l111_opy_ = bstack1lllll1l_opy_ (u"ࠣ࠼ࠥᕸ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠼ࠥᕹ") + bstack11llll1l111_opy_, bstack1l1ll1ll1ll_opy_)
    def bstack1l1ll1lll11_opy_(
        self,
        target: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll111l1_opy_, bstack1l1lll11111_opy_ = bstack1llll1l1lll_opy_
        bstack1l1lll1l1ll_opy_ = bstack1llll1lllll_opy_.bstack1l1lll11ll1_opy_(bstack1llll1l1lll_opy_)
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠥࡳࡳࡥࡨࡰࡱ࡮࠾ࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕺ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠦࠧᕻ"))
        if bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.QUIT:
            if bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.PRE:
                bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack1l111lll1l_opy_.value)
                bstack1lll1111l1l_opy_.bstack1llll11ll1l_opy_(instance, EVENTS.bstack1l111lll1l_opy_.value, bstack1ll111ll1l1_opy_)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠧ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠤᕼ").format(instance, method_name, bstack1l1lll111l1_opy_, bstack1l1lll11111_opy_))
        if bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.bstack1lllll11111_opy_:
            if bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.POST and not bstack1llll1lllll_opy_.bstack1lll1llll1l_opy_ in instance.data:
                session_id = getattr(target, bstack1lllll1l_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᕽ"), None)
                if session_id:
                    instance.data[bstack1llll1lllll_opy_.bstack1lll1llll1l_opy_] = session_id
        elif (
            bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_
            and bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args) == bstack1llll1lllll_opy_.bstack1llllll11ll_opy_
        ):
            if bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.PRE:
                hub_url = bstack1llll1lllll_opy_.bstack11l1l11lll_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1llll1lllll_opy_.bstack1lll1lllll1_opy_: hub_url,
                            bstack1llll1lllll_opy_.bstack1lll111l111_opy_: bstack1llll1lllll_opy_.bstack1lll1111111_opy_(hub_url),
                            bstack1llll1lllll_opy_.bstack1llllllllll_opy_: int(
                                os.environ.get(bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᕾ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1ll1l1ll1_opy_ = bstack1llll1lllll_opy_.bstack1l1lll1111l_opy_(*args)
                bstack11llll1l11l_opy_ = bstack1l1ll1l1ll1_opy_.get(bstack1lllll1l_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᕿ"), None) if bstack1l1ll1l1ll1_opy_ else None
                if isinstance(bstack11llll1l11l_opy_, dict):
                    instance.data[bstack1llll1lllll_opy_.bstack11llll1ll11_opy_] = copy.deepcopy(bstack11llll1l11l_opy_)
                    instance.data[bstack1llll1lllll_opy_.bstack1llll111l11_opy_] = bstack11llll1l11l_opy_
            elif bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1lllll1l_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣᖀ"), dict()).get(bstack1lllll1l_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡍࡩࠨᖁ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1llll1lllll_opy_.bstack1lll1llll1l_opy_: framework_session_id,
                                bstack1llll1lllll_opy_.bstack11llll1l1l1_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_
            and bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args) == bstack1llll1lllll_opy_.bstack11llll11lll_opy_
            and bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.POST
        ):
            instance.data[bstack1llll1lllll_opy_.bstack11llll1ll1l_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll1l1ll_opy_ in bstack1llll1lllll_opy_.bstack1l111111lll_opy_:
            bstack1l1ll1ll11l_opy_ = None
            for callback in bstack1llll1lllll_opy_.bstack1l111111lll_opy_[bstack1l1lll1l1ll_opy_]:
                try:
                    bstack1l1lll11l1l_opy_ = callback(self, target, exec, bstack1llll1l1lll_opy_, result, *args, **kwargs)
                    if bstack1l1ll1ll11l_opy_ == None:
                        bstack1l1ll1ll11l_opy_ = bstack1l1lll11l1l_opy_
                except Exception as e:
                    self.logger.error(bstack1lllll1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࠤᖂ") + str(e) + bstack1lllll1l_opy_ (u"ࠧࠨᖃ"))
                    traceback.print_exc()
            if bstack1l1lll111l1_opy_ == bstack1lllllll1l1_opy_.QUIT:
                if bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.POST:
                    bstack1ll111ll1l1_opy_ = bstack1lll1111l1l_opy_.get_state(instance, EVENTS.bstack1l111lll1l_opy_.value)
                    if bstack1ll111ll1l1_opy_!=None:
                        bstack1llllllll1l_opy_.end(EVENTS.bstack1l111lll1l_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᖄ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᖅ"), True, None)
            if bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.PRE and callable(bstack1l1ll1ll11l_opy_):
                return bstack1l1ll1ll11l_opy_
            elif bstack1l1lll11111_opy_ == bstack1llllll1l11_opy_.POST and bstack1l1ll1ll11l_opy_:
                return bstack1l1ll1ll11l_opy_
    def bstack1l1lll1l11l_opy_(
        self, method_name, previous_state: bstack1lllllll1l1_opy_, *args, **kwargs
    ) -> bstack1lllllll1l1_opy_:
        if method_name == bstack1lllll1l_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥᖆ") or method_name == bstack1lllll1l_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᖇ"):
            return bstack1lllllll1l1_opy_.bstack1lllll11111_opy_
        if method_name == bstack1lllll1l_opy_ (u"ࠥࡵࡺ࡯ࡴࠣᖈ"):
            return bstack1lllllll1l1_opy_.QUIT
        if method_name == bstack1lllll1l_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᖉ"):
            if previous_state != bstack1lllllll1l1_opy_.NONE:
                command_name = bstack1llll1lllll_opy_.bstack1llllllll11_opy_(*args)
                if command_name == bstack1llll1lllll_opy_.bstack1llllll11ll_opy_:
                    return bstack1lllllll1l1_opy_.bstack1lllll11111_opy_
            return bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_
        return bstack1lllllll1l1_opy_.NONE