# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import (
    bstack1lll1111l1l_opy_,
    bstack1llll1l1l11_opy_,
    bstack1llll11llll_opy_,
    bstack1llll11l1l1_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
from bstack_utils.constants import EVENTS
class bstack1llll11ll11_opy_(bstack1lll1111l1l_opy_):
    bstack1l1lll11ll1_opy_ = bstack11ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧᕠ")
    NAME = bstack11ll1l_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᕡ")
    bstack1lll11l1lll_opy_ = bstack11ll1l_opy_ (u"ࠢࡩࡷࡥࡣࡺࡸ࡬ࠣᕢ")
    bstack1lll1ll1l1l_opy_ = bstack11ll1l_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠣᕣ")
    bstack11llll11l1l_opy_ = bstack11ll1l_opy_ (u"ࠤ࡬ࡲࡵࡻࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᕤ")
    bstack1lll1l1111l_opy_ = bstack11ll1l_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᕥ")
    bstack1lll111llll_opy_ = bstack11ll1l_opy_ (u"ࠦ࡮ࡹ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡨࡶࡤࠥᕦ")
    bstack11llll111ll_opy_ = bstack11ll1l_opy_ (u"ࠧࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠤᕧ")
    bstack11llll1l11l_opy_ = bstack11ll1l_opy_ (u"ࠨࡥ࡯ࡦࡨࡨࡤࡧࡴࠣᕨ")
    bstack1lllll1llll_opy_ = bstack11ll1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࠣᕩ")
    bstack1llll11l11l_opy_ = bstack11ll1l_opy_ (u"ࠣࡰࡨࡻࡸ࡫ࡳࡴ࡫ࡲࡲࠧᕪ")
    bstack11llll11ll1_opy_ = bstack11ll1l_opy_ (u"ࠤࡪࡩࡹࠨᕫ")
    bstack1l111ll1l11_opy_ = bstack11ll1l_opy_ (u"ࠥࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠢᕬ")
    bstack1l1ll1ll1ll_opy_ = bstack11ll1l_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࠢᕭ")
    bstack1l1ll1l1111_opy_ = bstack11ll1l_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࡢࡵࡼࡲࡨࠨᕮ")
    bstack11llll1l111_opy_ = bstack11ll1l_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᕯ")
    bstack1l111111l1l_opy_: Dict[str, List[Callable]] = dict()
    bstack1llll1l11ll_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll11111_opy_: Any
    bstack1l1lll1111l_opy_: Dict
    def __init__(
        self,
        bstack1llll1l11ll_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lllll11111_opy_: Dict[str, Any],
        methods=[bstack11ll1l_opy_ (u"ࠢࡠࡡ࡬ࡲ࡮ࡺ࡟ࡠࠤᕰ"), bstack11ll1l_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣᕱ"), bstack11ll1l_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕲ"), bstack11ll1l_opy_ (u"ࠥࡵࡺ࡯ࡴࠣᕳ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llll1l11ll_opy_ = bstack1llll1l11ll_opy_
        self.platform_index = platform_index
        self.bstack1l1lll11l1l_opy_(methods)
        self.bstack1lllll11111_opy_ = bstack1lllll11111_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll11ll11_opy_.bstack1lll1ll1l1l_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll11ll11_opy_.bstack1lll11l1lll_opy_, target, strict)
    @staticmethod
    def bstack11llll11l11_opy_(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll11ll11_opy_.bstack11llll11l1l_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll1111l1l_opy_.get_data(bstack1llll11ll11_opy_.bstack1lll1l1111l_opy_, target, strict)
    @staticmethod
    def bstack1lll111l11l_opy_(instance: bstack1llll1l1l11_opy_) -> bool:
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll11ll11_opy_.bstack1lll111llll_opy_, False)
    @staticmethod
    def bstack1l1ll1ll11l_opy_(instance: bstack1llll1l1l11_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll11ll11_opy_.bstack1lll11l1lll_opy_, default_value)
    @staticmethod
    def bstack1l1lll111ll_opy_(instance: bstack1llll1l1l11_opy_, default_value=None):
        return bstack1lll1111l1l_opy_.get_state(instance, bstack1llll11ll11_opy_.bstack1lll1l1111l_opy_, default_value)
    @staticmethod
    def bstack1ll1lll1l11_opy_(hub_url: str, bstack11llll11lll_opy_=bstack11ll1l_opy_ (u"ࠦ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣᕴ")):
        try:
            bstack11llll111l1_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll111l1_opy_.endswith(bstack11llll11lll_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1ll1lll1l_opy_(method_name: str):
        return method_name == bstack11ll1l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᕵ")
    @staticmethod
    def bstack1lllll1ll11_opy_(method_name: str, *args):
        return (
            bstack1llll11ll11_opy_.bstack1l1ll1lll1l_opy_(method_name)
            and bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args) == bstack1llll11ll11_opy_.bstack1llll11l11l_opy_
        )
    @staticmethod
    def bstack1l1ll1lll11_opy_(method_name: str, *args):
        if not bstack1llll11ll11_opy_.bstack1l1ll1lll1l_opy_(method_name):
            return False
        if not bstack1llll11ll11_opy_.bstack1l1ll1ll1ll_opy_ in bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args):
            return False
        bstack1l1lll11111_opy_ = bstack1llll11ll11_opy_.bstack1l1ll1lllll_opy_(*args)
        return bstack1l1lll11111_opy_ and bstack11ll1l_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᕶ") in bstack1l1lll11111_opy_ and bstack11ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕷ") in bstack1l1lll11111_opy_[bstack11ll1l_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕸ")]
    @staticmethod
    def bstack1l1ll1l1l11_opy_(method_name: str, *args):
        if not bstack1llll11ll11_opy_.bstack1l1ll1lll1l_opy_(method_name):
            return False
        if not bstack1llll11ll11_opy_.bstack1l1ll1ll1ll_opy_ in bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args):
            return False
        bstack1l1lll11111_opy_ = bstack1llll11ll11_opy_.bstack1l1ll1lllll_opy_(*args)
        return (
            bstack1l1lll11111_opy_
            and bstack11ll1l_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕹ") in bstack1l1lll11111_opy_
            and bstack11ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡤࡴ࡬ࡴࡹࠨᕺ") in bstack1l1lll11111_opy_[bstack11ll1l_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕻ")]
        )
    @staticmethod
    def bstack1llllll1l1l_opy_(*args):
        return str(bstack1llll11ll11_opy_.bstack1l1ll1l1ll1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1ll1l1ll1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1lllll_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1llll1lll1_opy_(driver):
        command_executor = getattr(driver, bstack11ll1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕼ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack11ll1l_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦᕽ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack11ll1l_opy_ (u"ࠢࡠࡥ࡯࡭ࡪࡴࡴࡠࡥࡲࡲ࡫࡯ࡧࠣᕾ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack11ll1l_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥࡠࡵࡨࡶࡻ࡫ࡲࡠࡣࡧࡨࡷࠨᕿ"), None)
        return hub_url
    def bstack1llllll1lll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack11ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᖀ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack11ll1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᖁ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack11ll1l_opy_ (u"ࠦࡤࡻࡲ࡭ࠤᖂ")):
                setattr(command_executor, bstack11ll1l_opy_ (u"ࠧࡥࡵࡳ࡮ࠥᖃ"), hub_url)
                result = True
        if result:
            self.bstack1llll1l11ll_opy_ = hub_url
            bstack1llll11ll11_opy_.bstack1llll1l1lll_opy_(instance, bstack1llll11ll11_opy_.bstack1lll11l1lll_opy_, hub_url)
            bstack1llll11ll11_opy_.bstack1llll1l1lll_opy_(
                instance, bstack1llll11ll11_opy_.bstack1lll111llll_opy_, bstack1llll11ll11_opy_.bstack1ll1lll1l11_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_]):
        return bstack11ll1l_opy_ (u"ࠨ࠺ࠣᖄ").join((bstack1llll11llll_opy_(bstack1lllllllll1_opy_[0]).name, bstack1llll11l1l1_opy_(bstack1lllllllll1_opy_[1]).name))
    @staticmethod
    def bstack1lllll111ll_opy_(bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_], callback: Callable):
        bstack1l1ll1ll1l1_opy_ = bstack1llll11ll11_opy_.bstack1l1ll1l1l1l_opy_(bstack1lllllllll1_opy_)
        if not bstack1l1ll1ll1l1_opy_ in bstack1llll11ll11_opy_.bstack1l111111l1l_opy_:
            bstack1llll11ll11_opy_.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_] = []
        bstack1llll11ll11_opy_.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_].append(callback)
    def bstack1l1lll111l1_opy_(self, instance: bstack1llll1l1l11_opy_, method_name: str, bstack1l1lll11l11_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack11ll1l_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᖅ")):
            return
        cmd = args[0] if method_name == bstack11ll1l_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᖆ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1111l_opy_ = bstack11ll1l_opy_ (u"ࠤ࠽ࠦᖇ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠦᖈ") + bstack11llll1111l_opy_, bstack1l1lll11l11_opy_)
    def bstack1l1lll11lll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllllll1_opy_: Tuple[bstack1llll11llll_opy_, bstack1llll11l1l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1ll1l111l_opy_, bstack1l1ll1l1lll_opy_ = bstack1lllllllll1_opy_
        bstack1l1ll1ll1l1_opy_ = bstack1llll11ll11_opy_.bstack1l1ll1l1l1l_opy_(bstack1lllllllll1_opy_)
        self.logger.debug(bstack11ll1l_opy_ (u"ࠦࡴࡴ࡟ࡩࡱࡲ࡯࠿ࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᖉ") + str(kwargs) + bstack11ll1l_opy_ (u"ࠧࠨᖊ"))
        if bstack1l1ll1l111l_opy_ == bstack1llll11llll_opy_.QUIT:
            if bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.PRE:
                bstack1ll111l1l1l_opy_ = bstack1llll111ll1_opy_.bstack1ll1l111ll1_opy_(EVENTS.bstack11lll1l1ll_opy_.value)
                bstack1lll1111l1l_opy_.bstack1llll1l1lll_opy_(instance, EVENTS.bstack11lll1l1ll_opy_.value, bstack1ll111l1l1l_opy_)
                self.logger.debug(bstack11ll1l_opy_ (u"ࠨࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࢁࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡿࠣ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡿࠥᖋ").format(instance, method_name, bstack1l1ll1l111l_opy_, bstack1l1ll1l1lll_opy_))
        if bstack1l1ll1l111l_opy_ == bstack1llll11llll_opy_.bstack1llll11ll1l_opy_:
            if bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.POST and not bstack1llll11ll11_opy_.bstack1lll1ll1l1l_opy_ in instance.data:
                session_id = getattr(target, bstack11ll1l_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᖌ"), None)
                if session_id:
                    instance.data[bstack1llll11ll11_opy_.bstack1lll1ll1l1l_opy_] = session_id
        elif (
            bstack1l1ll1l111l_opy_ == bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_
            and bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args) == bstack1llll11ll11_opy_.bstack1llll11l11l_opy_
        ):
            if bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.PRE:
                hub_url = bstack1llll11ll11_opy_.bstack1llll1lll1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1llll11ll11_opy_.bstack1lll11l1lll_opy_: hub_url,
                            bstack1llll11ll11_opy_.bstack1lll111llll_opy_: bstack1llll11ll11_opy_.bstack1ll1lll1l11_opy_(hub_url),
                            bstack1llll11ll11_opy_.bstack1lllll1llll_opy_: int(
                                os.environ.get(bstack11ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᖍ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll11111_opy_ = bstack1llll11ll11_opy_.bstack1l1ll1lllll_opy_(*args)
                bstack11llll11l11_opy_ = bstack1l1lll11111_opy_.get(bstack11ll1l_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᖎ"), None) if bstack1l1lll11111_opy_ else None
                if isinstance(bstack11llll11l11_opy_, dict):
                    instance.data[bstack1llll11ll11_opy_.bstack11llll11l1l_opy_] = copy.deepcopy(bstack11llll11l11_opy_)
                    instance.data[bstack1llll11ll11_opy_.bstack1lll1l1111l_opy_] = bstack11llll11l11_opy_
            elif bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack11ll1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤᖏ"), dict()).get(bstack11ll1l_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡎࡪࠢᖐ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1llll11ll11_opy_.bstack1lll1ll1l1l_opy_: framework_session_id,
                                bstack1llll11ll11_opy_.bstack11llll111ll_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1ll1l111l_opy_ == bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_
            and bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args) == bstack1llll11ll11_opy_.bstack11llll1l111_opy_
            and bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.POST
        ):
            instance.data[bstack1llll11ll11_opy_.bstack11llll1l11l_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1ll1ll1l1_opy_ in bstack1llll11ll11_opy_.bstack1l111111l1l_opy_:
            bstack1l1ll1l11l1_opy_ = None
            for callback in bstack1llll11ll11_opy_.bstack1l111111l1l_opy_[bstack1l1ll1ll1l1_opy_]:
                try:
                    bstack1l1ll1l11ll_opy_ = callback(self, target, exec, bstack1lllllllll1_opy_, result, *args, **kwargs)
                    if bstack1l1ll1l11l1_opy_ == None:
                        bstack1l1ll1l11l1_opy_ = bstack1l1ll1l11ll_opy_
                except Exception as e:
                    self.logger.error(bstack11ll1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠤ࡮ࡴࡶࡰ࡭࡬ࡲ࡬ࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࠥᖑ") + str(e) + bstack11ll1l_opy_ (u"ࠨࠢᖒ"))
                    traceback.print_exc()
            if bstack1l1ll1l111l_opy_ == bstack1llll11llll_opy_.QUIT:
                if bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.POST:
                    bstack1ll111l1l1l_opy_ = bstack1lll1111l1l_opy_.get_state(instance, EVENTS.bstack11lll1l1ll_opy_.value)
                    if bstack1ll111l1l1l_opy_!=None:
                        bstack1llll111ll1_opy_.end(EVENTS.bstack11lll1l1ll_opy_.value, bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᖓ"), bstack1ll111l1l1l_opy_+bstack11ll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᖔ"), True, None)
            if bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.PRE and callable(bstack1l1ll1l11l1_opy_):
                return bstack1l1ll1l11l1_opy_
            elif bstack1l1ll1l1lll_opy_ == bstack1llll11l1l1_opy_.POST and bstack1l1ll1l11l1_opy_:
                return bstack1l1ll1l11l1_opy_
    def bstack1l1ll1llll1_opy_(
        self, method_name, previous_state: bstack1llll11llll_opy_, *args, **kwargs
    ) -> bstack1llll11llll_opy_:
        if method_name == bstack11ll1l_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦᖕ") or method_name == bstack11ll1l_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᖖ"):
            return bstack1llll11llll_opy_.bstack1llll11ll1l_opy_
        if method_name == bstack11ll1l_opy_ (u"ࠦࡶࡻࡩࡵࠤᖗ"):
            return bstack1llll11llll_opy_.QUIT
        if method_name == bstack11ll1l_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᖘ"):
            if previous_state != bstack1llll11llll_opy_.NONE:
                command_name = bstack1llll11ll11_opy_.bstack1llllll1l1l_opy_(*args)
                if command_name == bstack1llll11ll11_opy_.bstack1llll11l11l_opy_:
                    return bstack1llll11llll_opy_.bstack1llll11ll1l_opy_
            return bstack1llll11llll_opy_.bstack1llll1ll1l1_opy_
        return bstack1llll11llll_opy_.NONE