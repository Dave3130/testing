# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll1l1ll_opy_ import (
    bstack1lll11l1111_opy_,
    bstack1llll1l1111_opy_,
    bstack1lllll1lll1_opy_,
    bstack1llll1l1lll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll11l1l_opy_(bstack1lll11l1111_opy_):
    bstack1l1ll1ll11l_opy_ = bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝ࠨᕓ")
    NAME = bstack11l111_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᕔ")
    bstack1llll111ll1_opy_ = bstack11l111_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭ࠤᕕ")
    bstack1lll1ll1l11_opy_ = bstack11l111_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠤᕖ")
    bstack11llll1ll11_opy_ = bstack11l111_opy_ (u"ࠥ࡭ࡳࡶࡵࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᕗ")
    bstack1lll1ll1111_opy_ = bstack11l111_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᕘ")
    bstack1lll11l11ll_opy_ = bstack11l111_opy_ (u"ࠧ࡯ࡳࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡩࡷࡥࠦᕙ")
    bstack11llll1l11l_opy_ = bstack11l111_opy_ (u"ࠨࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᕚ")
    bstack11llll1l111_opy_ = bstack11l111_opy_ (u"ࠢࡦࡰࡧࡩࡩࡥࡡࡵࠤᕛ")
    bstack1llllllll11_opy_ = bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࠤᕜ")
    bstack1llll11l1ll_opy_ = bstack11l111_opy_ (u"ࠤࡱࡩࡼࡹࡥࡴࡵ࡬ࡳࡳࠨᕝ")
    bstack11llll1l1ll_opy_ = bstack11l111_opy_ (u"ࠥ࡫ࡪࡺࠢᕞ")
    bstack1l11l1l11ll_opy_ = bstack11l111_opy_ (u"ࠦࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠣᕟ")
    bstack1l1lll1l1ll_opy_ = bstack11l111_opy_ (u"ࠧࡽ࠳ࡤࡧࡻࡩࡨࡻࡴࡦࡵࡦࡶ࡮ࡶࡴࠣᕠ")
    bstack1l1lll1l11l_opy_ = bstack11l111_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࡣࡶࡽࡳࡩࠢᕡ")
    bstack11llll11l1l_opy_ = bstack11l111_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᕢ")
    bstack1l11111l1l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1lllll11l11_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llllll1ll1_opy_: Any
    bstack1l1ll1llll1_opy_: Dict
    def __init__(
        self,
        bstack1lllll11l11_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llllll1ll1_opy_: Dict[str, Any],
        methods=[bstack11l111_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥᕣ"), bstack11l111_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᕤ"), bstack11l111_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᕥ"), bstack11l111_opy_ (u"ࠦࡶࡻࡩࡵࠤᕦ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1lllll11l11_opy_ = bstack1lllll11l11_opy_
        self.platform_index = platform_index
        self.bstack1l1lll11111_opy_(methods)
        self.bstack1llllll1ll1_opy_ = bstack1llllll1ll1_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l1l_opy_.bstack1lll1ll1l11_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l1l_opy_.bstack1llll111ll1_opy_, target, strict)
    @staticmethod
    def bstack11llll1ll1l_opy_(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l1l_opy_.bstack11llll1ll11_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll11l1111_opy_.get_data(bstack1lllll11l1l_opy_.bstack1lll1ll1111_opy_, target, strict)
    @staticmethod
    def bstack1lll111l11l_opy_(instance: bstack1llll1l1111_opy_) -> bool:
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lllll11l1l_opy_.bstack1lll11l11ll_opy_, False)
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1llll1l1111_opy_, default_value=None):
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lllll11l1l_opy_.bstack1llll111ll1_opy_, default_value)
    @staticmethod
    def bstack1l1ll1ll1ll_opy_(instance: bstack1llll1l1111_opy_, default_value=None):
        return bstack1lll11l1111_opy_.get_state(instance, bstack1lllll11l1l_opy_.bstack1lll1ll1111_opy_, default_value)
    @staticmethod
    def bstack1ll1llll1l1_opy_(hub_url: str, bstack11llll1l1l1_opy_=bstack11l111_opy_ (u"ࠧ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤᕧ")):
        try:
            bstack11llll11lll_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll11lll_opy_.endswith(bstack11llll1l1l1_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1ll1lllll_opy_(method_name: str):
        return method_name == bstack11l111_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᕨ")
    @staticmethod
    def bstack1lllll1l11l_opy_(method_name: str, *args):
        return (
            bstack1lllll11l1l_opy_.bstack1l1ll1lllll_opy_(method_name)
            and bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args) == bstack1lllll11l1l_opy_.bstack1llll11l1ll_opy_
        )
    @staticmethod
    def bstack1l1ll1lll11_opy_(method_name: str, *args):
        if not bstack1lllll11l1l_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lllll11l1l_opy_.bstack1l1lll1l1ll_opy_ in bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args):
            return False
        bstack1l1ll1l1l11_opy_ = bstack1lllll11l1l_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return bstack1l1ll1l1l11_opy_ and bstack11l111_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕩ") in bstack1l1ll1l1l11_opy_ and bstack11l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕪ") in bstack1l1ll1l1l11_opy_[bstack11l111_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕫ")]
    @staticmethod
    def bstack1l1lll111l1_opy_(method_name: str, *args):
        if not bstack1lllll11l1l_opy_.bstack1l1ll1lllll_opy_(method_name):
            return False
        if not bstack1lllll11l1l_opy_.bstack1l1lll1l1ll_opy_ in bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args):
            return False
        bstack1l1ll1l1l11_opy_ = bstack1lllll11l1l_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return (
            bstack1l1ll1l1l11_opy_
            and bstack11l111_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕬ") in bstack1l1ll1l1l11_opy_
            and bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡥࡵ࡭ࡵࡺࠢᕭ") in bstack1l1ll1l1l11_opy_[bstack11l111_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕮ")]
        )
    @staticmethod
    def bstack1llllll11ll_opy_(*args):
        return str(bstack1lllll11l1l_opy_.bstack1l1lll1111l_opy_(*args)).lower()
    @staticmethod
    def bstack1l1lll1111l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack1111llll1_opy_(driver):
        command_executor = getattr(driver, bstack11l111_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕯ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack11l111_opy_ (u"ࠢࡠࡷࡵࡰࠧᕰ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack11l111_opy_ (u"ࠣࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠤᕱ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack11l111_opy_ (u"ࠤࡵࡩࡲࡵࡴࡦࡡࡶࡩࡷࡼࡥࡳࡡࡤࡨࡩࡸࠢᕲ"), None)
        return hub_url
    def bstack1lllll1llll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack11l111_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨᕳ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᕴ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack11l111_opy_ (u"ࠧࡥࡵࡳ࡮ࠥᕵ")):
                setattr(command_executor, bstack11l111_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦᕶ"), hub_url)
                result = True
        if result:
            self.bstack1lllll11l11_opy_ = hub_url
            bstack1lllll11l1l_opy_.bstack1llllllll1l_opy_(instance, bstack1lllll11l1l_opy_.bstack1llll111ll1_opy_, hub_url)
            bstack1lllll11l1l_opy_.bstack1llllllll1l_opy_(
                instance, bstack1lllll11l1l_opy_.bstack1lll11l11ll_opy_, bstack1lllll11l1l_opy_.bstack1ll1llll1l1_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1ll1lll1l_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_]):
        return bstack11l111_opy_ (u"ࠢ࠻ࠤᕷ").join((bstack1lllll1lll1_opy_(bstack1lllll1ll11_opy_[0]).name, bstack1llll1l1lll_opy_(bstack1lllll1ll11_opy_[1]).name))
    @staticmethod
    def bstack1lllllll11l_opy_(bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_], callback: Callable):
        bstack1l1ll1ll111_opy_ = bstack1lllll11l1l_opy_.bstack1l1ll1lll1l_opy_(bstack1lllll1ll11_opy_)
        if not bstack1l1ll1ll111_opy_ in bstack1lllll11l1l_opy_.bstack1l11111l1l1_opy_:
            bstack1lllll11l1l_opy_.bstack1l11111l1l1_opy_[bstack1l1ll1ll111_opy_] = []
        bstack1lllll11l1l_opy_.bstack1l11111l1l1_opy_[bstack1l1ll1ll111_opy_].append(callback)
    def bstack1l1lll1l111_opy_(self, instance: bstack1llll1l1111_opy_, method_name: str, bstack1l1lll111ll_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack11l111_opy_ (u"ࠣࡵࡷࡥࡷࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠣᕸ")):
            return
        cmd = args[0] if method_name == bstack11l111_opy_ (u"ࠤࡨࡼࡪࡩࡵࡵࡧࠥᕹ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll11ll1_opy_ = bstack11l111_opy_ (u"ࠥ࠾ࠧᕺ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠧᕻ") + bstack11llll11ll1_opy_, bstack1l1lll111ll_opy_)
    def bstack1l1ll1l1lll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1l1111_opy_, str],
        bstack1lllll1ll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1l1lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1ll1l1ll1_opy_, bstack1l1lll11ll1_opy_ = bstack1lllll1ll11_opy_
        bstack1l1ll1ll111_opy_ = bstack1lllll11l1l_opy_.bstack1l1ll1lll1l_opy_(bstack1lllll1ll11_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠧࡵ࡮ࡠࡪࡲࡳࡰࡀࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᕼ") + str(kwargs) + bstack11l111_opy_ (u"ࠨࠢᕽ"))
        if bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.QUIT:
            if bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.PRE:
                bstack1ll1l1l11l1_opy_ = bstack1llll11ll11_opy_.bstack1ll11l11ll1_opy_(EVENTS.bstack1l1l11lll_opy_.value)
                bstack1lll11l1111_opy_.bstack1llllllll1l_opy_(instance, EVENTS.bstack1l1l11lll_opy_.value, bstack1ll1l1l11l1_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠢࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࢂࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠦᕾ").format(instance, method_name, bstack1l1ll1l1ll1_opy_, bstack1l1lll11ll1_opy_))
        if bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.bstack1llll11llll_opy_:
            if bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.POST and not bstack1lllll11l1l_opy_.bstack1lll1ll1l11_opy_ in instance.data:
                session_id = getattr(target, bstack11l111_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠧᕿ"), None)
                if session_id:
                    instance.data[bstack1lllll11l1l_opy_.bstack1lll1ll1l11_opy_] = session_id
        elif (
            bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_
            and bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args) == bstack1lllll11l1l_opy_.bstack1llll11l1ll_opy_
        ):
            if bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.PRE:
                hub_url = bstack1lllll11l1l_opy_.bstack1111llll1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll11l1l_opy_.bstack1llll111ll1_opy_: hub_url,
                            bstack1lllll11l1l_opy_.bstack1lll11l11ll_opy_: bstack1lllll11l1l_opy_.bstack1ll1llll1l1_opy_(hub_url),
                            bstack1lllll11l1l_opy_.bstack1llllllll11_opy_: int(
                                os.environ.get(bstack11l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠤᖀ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1ll1l1l11_opy_ = bstack1lllll11l1l_opy_.bstack1l1ll1ll1l1_opy_(*args)
                bstack11llll1ll1l_opy_ = bstack1l1ll1l1l11_opy_.get(bstack11l111_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᖁ"), None) if bstack1l1ll1l1l11_opy_ else None
                if isinstance(bstack11llll1ll1l_opy_, dict):
                    instance.data[bstack1lllll11l1l_opy_.bstack11llll1ll11_opy_] = copy.deepcopy(bstack11llll1ll1l_opy_)
                    instance.data[bstack1lllll11l1l_opy_.bstack1lll1ll1111_opy_] = bstack11llll1ll1l_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack11l111_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥᖂ"), dict()).get(bstack11l111_opy_ (u"ࠧࡹࡥࡴࡵ࡬ࡳࡳࡏࡤࠣᖃ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll11l1l_opy_.bstack1lll1ll1l11_opy_: framework_session_id,
                                bstack1lllll11l1l_opy_.bstack11llll1l11l_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_
            and bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args) == bstack1lllll11l1l_opy_.bstack11llll11l1l_opy_
            and bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.POST
        ):
            instance.data[bstack1lllll11l1l_opy_.bstack11llll1l111_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1ll1ll111_opy_ in bstack1lllll11l1l_opy_.bstack1l11111l1l1_opy_:
            bstack1l1lll11lll_opy_ = None
            for callback in bstack1lllll11l1l_opy_.bstack1l11111l1l1_opy_[bstack1l1ll1ll111_opy_]:
                try:
                    bstack1l1ll1l1l1l_opy_ = callback(self, target, exec, bstack1lllll1ll11_opy_, result, *args, **kwargs)
                    if bstack1l1lll11lll_opy_ == None:
                        bstack1l1lll11lll_opy_ = bstack1l1ll1l1l1l_opy_
                except Exception as e:
                    self.logger.error(bstack11l111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠥ࡯࡮ࡷࡱ࡮࡭ࡳ࡭ࠠࡤࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࠦᖄ") + str(e) + bstack11l111_opy_ (u"ࠢࠣᖅ"))
                    traceback.print_exc()
            if bstack1l1ll1l1ll1_opy_ == bstack1lllll1lll1_opy_.QUIT:
                if bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.POST:
                    bstack1ll1l1l11l1_opy_ = bstack1lll11l1111_opy_.get_state(instance, EVENTS.bstack1l1l11lll_opy_.value)
                    if bstack1ll1l1l11l1_opy_!=None:
                        bstack1llll11ll11_opy_.end(EVENTS.bstack1l1l11lll_opy_.value, bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᖆ"), bstack1ll1l1l11l1_opy_+bstack11l111_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᖇ"), True, None)
            if bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.PRE and callable(bstack1l1lll11lll_opy_):
                return bstack1l1lll11lll_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1llll1l1lll_opy_.POST and bstack1l1lll11lll_opy_:
                return bstack1l1lll11lll_opy_
    def bstack1l1lll11l1l_opy_(
        self, method_name, previous_state: bstack1lllll1lll1_opy_, *args, **kwargs
    ) -> bstack1lllll1lll1_opy_:
        if method_name == bstack11l111_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧᖈ") or method_name == bstack11l111_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᖉ"):
            return bstack1lllll1lll1_opy_.bstack1llll11llll_opy_
        if method_name == bstack11l111_opy_ (u"ࠧࡷࡵࡪࡶࠥᖊ"):
            return bstack1lllll1lll1_opy_.QUIT
        if method_name == bstack11l111_opy_ (u"ࠨࡥࡹࡧࡦࡹࡹ࡫ࠢᖋ"):
            if previous_state != bstack1lllll1lll1_opy_.NONE:
                command_name = bstack1lllll11l1l_opy_.bstack1llllll11ll_opy_(*args)
                if command_name == bstack1lllll11l1l_opy_.bstack1llll11l1ll_opy_:
                    return bstack1lllll1lll1_opy_.bstack1llll11llll_opy_
            return bstack1lllll1lll1_opy_.bstack1llllll11l1_opy_
        return bstack1lllll1lll1_opy_.NONE