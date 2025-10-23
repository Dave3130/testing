# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lll1111lll_opy_,
    bstack1llll11l11l_opy_,
    bstack1lllll111ll_opy_,
    bstack1llllll1l11_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1111l111l1_opy_ import bstack1lllllll111_opy_
from bstack_utils.constants import EVENTS
class bstack1lllll1l11l_opy_(bstack1lll1111lll_opy_):
    bstack1l1ll1ll1ll_opy_ = bstack11lll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᕍ")
    NAME = bstack11lll1_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᕎ")
    bstack1lll1l1l11l_opy_ = bstack11lll1_opy_ (u"ࠤ࡫ࡹࡧࡥࡵࡳ࡮ࠥᕏ")
    bstack1lll1l1l1ll_opy_ = bstack11lll1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᕐ")
    bstack11llll1l1ll_opy_ = bstack11lll1_opy_ (u"ࠦ࡮ࡴࡰࡶࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᕑ")
    bstack1lll11ll1ll_opy_ = bstack11lll1_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᕒ")
    bstack1lll11l11l1_opy_ = bstack11lll1_opy_ (u"ࠨࡩࡴࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡪࡸࡦࠧᕓ")
    bstack11llll1l1l1_opy_ = bstack11lll1_opy_ (u"ࠢࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᕔ")
    bstack11llll1l11l_opy_ = bstack11lll1_opy_ (u"ࠣࡧࡱࡨࡪࡪ࡟ࡢࡶࠥᕕ")
    bstack1llll1ll111_opy_ = bstack11lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࠥᕖ")
    bstack1llll1lllll_opy_ = bstack11lll1_opy_ (u"ࠥࡲࡪࡽࡳࡦࡵࡶ࡭ࡴࡴࠢᕗ")
    bstack11llll11lll_opy_ = bstack11lll1_opy_ (u"ࠦ࡬࡫ࡴࠣᕘ")
    bstack1l111ll1ll1_opy_ = bstack11lll1_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᕙ")
    bstack1l1ll1l1l11_opy_ = bstack11lll1_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࠤᕚ")
    bstack1l1lll11l11_opy_ = bstack11lll1_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࡤࡷࡾࡴࡣࠣᕛ")
    bstack11llll11l1l_opy_ = bstack11lll1_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᕜ")
    bstack1l11111l1l1_opy_: Dict[str, List[Callable]] = dict()
    bstack1lllll1l1ll_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1llll1l111l_opy_: Any
    bstack1l1ll1ll11l_opy_: Dict
    def __init__(
        self,
        bstack1lllll1l1ll_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1llll1l111l_opy_: Dict[str, Any],
        methods=[bstack11lll1_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦᕝ"), bstack11lll1_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕞ"), bstack11lll1_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕟ"), bstack11lll1_opy_ (u"ࠧࡷࡵࡪࡶࠥᕠ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1lllll1l1ll_opy_ = bstack1lllll1l1ll_opy_
        self.platform_index = platform_index
        self.bstack1l1ll1llll1_opy_(methods)
        self.bstack1llll1l111l_opy_ = bstack1llll1l111l_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll1111lll_opy_.get_data(bstack1lllll1l11l_opy_.bstack1lll1l1l1ll_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll1111lll_opy_.get_data(bstack1lllll1l11l_opy_.bstack1lll1l1l11l_opy_, target, strict)
    @staticmethod
    def bstack11llll11l11_opy_(target: object, strict=True):
        return bstack1lll1111lll_opy_.get_data(bstack1lllll1l11l_opy_.bstack11llll1l1ll_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll1111lll_opy_.get_data(bstack1lllll1l11l_opy_.bstack1lll11ll1ll_opy_, target, strict)
    @staticmethod
    def bstack1lll111l1ll_opy_(instance: bstack1llll11l11l_opy_) -> bool:
        return bstack1lll1111lll_opy_.get_state(instance, bstack1lllll1l11l_opy_.bstack1lll11l11l1_opy_, False)
    @staticmethod
    def bstack1l1lll1l111_opy_(instance: bstack1llll11l11l_opy_, default_value=None):
        return bstack1lll1111lll_opy_.get_state(instance, bstack1lllll1l11l_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1l1ll1l1lll_opy_(instance: bstack1llll11l11l_opy_, default_value=None):
        return bstack1lll1111lll_opy_.get_state(instance, bstack1lllll1l11l_opy_.bstack1lll11ll1ll_opy_, default_value)
    @staticmethod
    def bstack1ll1llll111_opy_(hub_url: str, bstack11llll11ll1_opy_=bstack11lll1_opy_ (u"ࠨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᕡ")):
        try:
            bstack11llll1ll11_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll1ll11_opy_.endswith(bstack11llll11ll1_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll111l1_opy_(method_name: str):
        return method_name == bstack11lll1_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᕢ")
    @staticmethod
    def bstack1llll11l1ll_opy_(method_name: str, *args):
        return (
            bstack1lllll1l11l_opy_.bstack1l1lll111l1_opy_(method_name)
            and bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args) == bstack1lllll1l11l_opy_.bstack1llll1lllll_opy_
        )
    @staticmethod
    def bstack1l1ll1l1l1l_opy_(method_name: str, *args):
        if not bstack1lllll1l11l_opy_.bstack1l1lll111l1_opy_(method_name):
            return False
        if not bstack1lllll1l11l_opy_.bstack1l1ll1l1l11_opy_ in bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args):
            return False
        bstack1l1ll1lll11_opy_ = bstack1lllll1l11l_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return bstack1l1ll1lll11_opy_ and bstack11lll1_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕣ") in bstack1l1ll1lll11_opy_ and bstack11lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕤ") in bstack1l1ll1lll11_opy_[bstack11lll1_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᕥ")]
    @staticmethod
    def bstack1l1lll11lll_opy_(method_name: str, *args):
        if not bstack1lllll1l11l_opy_.bstack1l1lll111l1_opy_(method_name):
            return False
        if not bstack1lllll1l11l_opy_.bstack1l1ll1l1l11_opy_ in bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args):
            return False
        bstack1l1ll1lll11_opy_ = bstack1lllll1l11l_opy_.bstack1l1ll1ll1l1_opy_(*args)
        return (
            bstack1l1ll1lll11_opy_
            and bstack11lll1_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕦ") in bstack1l1ll1lll11_opy_
            and bstack11lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡦࡶ࡮ࡶࡴࠣᕧ") in bstack1l1ll1lll11_opy_[bstack11lll1_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᕨ")]
        )
    @staticmethod
    def bstack1llll11ll11_opy_(*args):
        return str(bstack1lllll1l11l_opy_.bstack1l1lll1l11l_opy_(*args)).lower()
    @staticmethod
    def bstack1l1lll1l11l_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1ll1l1_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11lll1lll1_opy_(driver):
        command_executor = getattr(driver, bstack11lll1_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᕩ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack11lll1_opy_ (u"ࠣࡡࡸࡶࡱࠨᕪ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack11lll1_opy_ (u"ࠤࡢࡧࡱ࡯ࡥ࡯ࡶࡢࡧࡴࡴࡦࡪࡩࠥᕫ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack11lll1_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡢࡷࡪࡸࡶࡦࡴࡢࡥࡩࡪࡲࠣᕬ"), None)
        return hub_url
    def bstack1llllllllll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack11lll1_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᕭ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack11lll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕮ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack11lll1_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦᕯ")):
                setattr(command_executor, bstack11lll1_opy_ (u"ࠢࡠࡷࡵࡰࠧᕰ"), hub_url)
                result = True
        if result:
            self.bstack1lllll1l1ll_opy_ = hub_url
            bstack1lllll1l11l_opy_.bstack1lllll11l11_opy_(instance, bstack1lllll1l11l_opy_.bstack1lll1l1l11l_opy_, hub_url)
            bstack1lllll1l11l_opy_.bstack1lllll11l11_opy_(
                instance, bstack1lllll1l11l_opy_.bstack1lll11l11l1_opy_, bstack1lllll1l11l_opy_.bstack1ll1llll111_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1ll1l11ll_opy_(bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_]):
        return bstack11lll1_opy_ (u"ࠣ࠼ࠥᕱ").join((bstack1lllll111ll_opy_(bstack1llll1lll1l_opy_[0]).name, bstack1llllll1l11_opy_(bstack1llll1lll1l_opy_[1]).name))
    @staticmethod
    def bstack1lllll1llll_opy_(bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_], callback: Callable):
        bstack1l1ll1ll111_opy_ = bstack1lllll1l11l_opy_.bstack1l1ll1l11ll_opy_(bstack1llll1lll1l_opy_)
        if not bstack1l1ll1ll111_opy_ in bstack1lllll1l11l_opy_.bstack1l11111l1l1_opy_:
            bstack1lllll1l11l_opy_.bstack1l11111l1l1_opy_[bstack1l1ll1ll111_opy_] = []
        bstack1lllll1l11l_opy_.bstack1l11111l1l1_opy_[bstack1l1ll1ll111_opy_].append(callback)
    def bstack1l1lll11111_opy_(self, instance: bstack1llll11l11l_opy_, method_name: str, bstack1l1lll1111l_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack11lll1_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᕲ")):
            return
        cmd = args[0] if method_name == bstack11lll1_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᕳ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1l111_opy_ = bstack11lll1_opy_ (u"ࠦ࠿ࠨᕴ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠨᕵ") + bstack11llll1l111_opy_, bstack1l1lll1111l_opy_)
    def bstack1l1lll1l1l1_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll11l11l_opy_, str],
        bstack1llll1lll1l_opy_: Tuple[bstack1lllll111ll_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1lll111ll_opy_, bstack1l1lll11ll1_opy_ = bstack1llll1lll1l_opy_
        bstack1l1ll1ll111_opy_ = bstack1lllll1l11l_opy_.bstack1l1ll1l11ll_opy_(bstack1llll1lll1l_opy_)
        self.logger.debug(bstack11lll1_opy_ (u"ࠨ࡯࡯ࡡ࡫ࡳࡴࡱ࠺ࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᕶ") + str(kwargs) + bstack11lll1_opy_ (u"ࠢࠣᕷ"))
        if bstack1l1lll111ll_opy_ == bstack1lllll111ll_opy_.QUIT:
            if bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.PRE:
                bstack1ll1l1111ll_opy_ = bstack1lllllll111_opy_.bstack1ll11111l1l_opy_(EVENTS.bstack111lll1l11_opy_.value)
                bstack1lll1111lll_opy_.bstack1lllll11l11_opy_(instance, EVENTS.bstack111lll1l11_opy_.value, bstack1ll1l1111ll_opy_)
                self.logger.debug(bstack11lll1_opy_ (u"ࠣ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠧᕸ").format(instance, method_name, bstack1l1lll111ll_opy_, bstack1l1lll11ll1_opy_))
        if bstack1l1lll111ll_opy_ == bstack1lllll111ll_opy_.bstack1llllll1lll_opy_:
            if bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.POST and not bstack1lllll1l11l_opy_.bstack1lll1l1l1ll_opy_ in instance.data:
                session_id = getattr(target, bstack11lll1_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᕹ"), None)
                if session_id:
                    instance.data[bstack1lllll1l11l_opy_.bstack1lll1l1l1ll_opy_] = session_id
        elif (
            bstack1l1lll111ll_opy_ == bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_
            and bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args) == bstack1lllll1l11l_opy_.bstack1llll1lllll_opy_
        ):
            if bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.PRE:
                hub_url = bstack1lllll1l11l_opy_.bstack11lll1lll1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllll1l11l_opy_.bstack1lll1l1l11l_opy_: hub_url,
                            bstack1lllll1l11l_opy_.bstack1lll11l11l1_opy_: bstack1lllll1l11l_opy_.bstack1ll1llll111_opy_(hub_url),
                            bstack1lllll1l11l_opy_.bstack1llll1ll111_opy_: int(
                                os.environ.get(bstack11lll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥᕺ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1ll1lll11_opy_ = bstack1lllll1l11l_opy_.bstack1l1ll1ll1l1_opy_(*args)
                bstack11llll11l11_opy_ = bstack1l1ll1lll11_opy_.get(bstack11lll1_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᕻ"), None) if bstack1l1ll1lll11_opy_ else None
                if isinstance(bstack11llll11l11_opy_, dict):
                    instance.data[bstack1lllll1l11l_opy_.bstack11llll1l1ll_opy_] = copy.deepcopy(bstack11llll11l11_opy_)
                    instance.data[bstack1lllll1l11l_opy_.bstack1lll11ll1ll_opy_] = bstack11llll11l11_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack11lll1_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᕼ"), dict()).get(bstack11lll1_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤᕽ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllll1l11l_opy_.bstack1lll1l1l1ll_opy_: framework_session_id,
                                bstack1lllll1l11l_opy_.bstack11llll1l1l1_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1lll111ll_opy_ == bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_
            and bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args) == bstack1lllll1l11l_opy_.bstack11llll11l1l_opy_
            and bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.POST
        ):
            instance.data[bstack1lllll1l11l_opy_.bstack11llll1l11l_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1ll1ll111_opy_ in bstack1lllll1l11l_opy_.bstack1l11111l1l1_opy_:
            bstack1l1ll1lll1l_opy_ = None
            for callback in bstack1lllll1l11l_opy_.bstack1l11111l1l1_opy_[bstack1l1ll1ll111_opy_]:
                try:
                    bstack1l1ll1l1ll1_opy_ = callback(self, target, exec, bstack1llll1lll1l_opy_, result, *args, **kwargs)
                    if bstack1l1ll1lll1l_opy_ == None:
                        bstack1l1ll1lll1l_opy_ = bstack1l1ll1l1ll1_opy_
                except Exception as e:
                    self.logger.error(bstack11lll1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࠧᕾ") + str(e) + bstack11lll1_opy_ (u"ࠣࠤᕿ"))
                    traceback.print_exc()
            if bstack1l1lll111ll_opy_ == bstack1lllll111ll_opy_.QUIT:
                if bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.POST:
                    bstack1ll1l1111ll_opy_ = bstack1lll1111lll_opy_.get_state(instance, EVENTS.bstack111lll1l11_opy_.value)
                    if bstack1ll1l1111ll_opy_!=None:
                        bstack1lllllll111_opy_.end(EVENTS.bstack111lll1l11_opy_.value, bstack1ll1l1111ll_opy_+bstack11lll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᖀ"), bstack1ll1l1111ll_opy_+bstack11lll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᖁ"), True, None)
            if bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.PRE and callable(bstack1l1ll1lll1l_opy_):
                return bstack1l1ll1lll1l_opy_
            elif bstack1l1lll11ll1_opy_ == bstack1llllll1l11_opy_.POST and bstack1l1ll1lll1l_opy_:
                return bstack1l1ll1lll1l_opy_
    def bstack1l1lll11l1l_opy_(
        self, method_name, previous_state: bstack1lllll111ll_opy_, *args, **kwargs
    ) -> bstack1lllll111ll_opy_:
        if method_name == bstack11lll1_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨᖂ") or method_name == bstack11lll1_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᖃ"):
            return bstack1lllll111ll_opy_.bstack1llllll1lll_opy_
        if method_name == bstack11lll1_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᖄ"):
            return bstack1lllll111ll_opy_.QUIT
        if method_name == bstack11lll1_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᖅ"):
            if previous_state != bstack1lllll111ll_opy_.NONE:
                command_name = bstack1lllll1l11l_opy_.bstack1llll11ll11_opy_(*args)
                if command_name == bstack1lllll1l11l_opy_.bstack1llll1lllll_opy_:
                    return bstack1lllll111ll_opy_.bstack1llllll1lll_opy_
            return bstack1lllll111ll_opy_.bstack1llll1l1ll1_opy_
        return bstack1lllll111ll_opy_.NONE