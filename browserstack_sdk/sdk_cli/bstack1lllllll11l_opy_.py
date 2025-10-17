# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import (
    bstack1lll11ll11l_opy_,
    bstack1llllll1lll_opy_,
    bstack1lllll11111_opy_,
    bstack1llllllll1l_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
from bstack_utils.constants import EVENTS
class bstack1lllllll1ll_opy_(bstack1lll11ll11l_opy_):
    bstack1l1lll1ll1l_opy_ = bstack11l111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᔠ")
    NAME = bstack11l111_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢᔡ")
    bstack1lll1l1l11l_opy_ = bstack11l111_opy_ (u"ࠨࡨࡶࡤࡢࡹࡷࡲࠢᔢ")
    bstack1llll111l11_opy_ = bstack11l111_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᔣ")
    bstack11lllll1111_opy_ = bstack11l111_opy_ (u"ࠣ࡫ࡱࡴࡺࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᔤ")
    bstack1lll1l1llll_opy_ = bstack11l111_opy_ (u"ࠤࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᔥ")
    bstack1lll11l1l1l_opy_ = bstack11l111_opy_ (u"ࠥ࡭ࡸࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡮ࡵࡣࠤᔦ")
    bstack11lllll11ll_opy_ = bstack11l111_opy_ (u"ࠦࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᔧ")
    bstack11lllll1l11_opy_ = bstack11l111_opy_ (u"ࠧ࡫࡮ࡥࡧࡧࡣࡦࡺࠢᔨ")
    bstack1111111l1l_opy_ = bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠢᔩ")
    bstack1111111lll_opy_ = bstack11l111_opy_ (u"ࠢ࡯ࡧࡺࡷࡪࡹࡳࡪࡱࡱࠦᔪ")
    bstack11lllll111l_opy_ = bstack11l111_opy_ (u"ࠣࡩࡨࡸࠧᔫ")
    bstack1l11l11ll11_opy_ = bstack11l111_opy_ (u"ࠤࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࠨᔬ")
    bstack1l1lll11lll_opy_ = bstack11l111_opy_ (u"ࠥࡻ࠸ࡩࡥࡹࡧࡦࡹࡹ࡫ࡳࡤࡴ࡬ࡴࡹࠨᔭ")
    bstack1l1ll1llll1_opy_ = bstack11l111_opy_ (u"ࠦࡼ࠹ࡣࡦࡺࡨࡧࡺࡺࡥࡴࡥࡵ࡭ࡵࡺࡡࡴࡻࡱࡧࠧᔮ")
    bstack11llll1llll_opy_ = bstack11l111_opy_ (u"ࠧࡷࡵࡪࡶࠥᔯ")
    bstack1l1111l111l_opy_: Dict[str, List[Callable]] = dict()
    bstack1llllll1l1l_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll1llll_opy_: Any
    bstack1l1lll1l1l1_opy_: Dict
    def __init__(
        self,
        bstack1llllll1l1l_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lllll1llll_opy_: Dict[str, Any],
        methods=[bstack11l111_opy_ (u"ࠨ࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠣᔰ"), bstack11l111_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᔱ"), bstack11l111_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᔲ"), bstack11l111_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᔳ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1llllll1l1l_opy_ = bstack1llllll1l1l_opy_
        self.platform_index = platform_index
        self.bstack1l1ll1lllll_opy_(methods)
        self.bstack1lllll1llll_opy_ = bstack1lllll1llll_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll11ll11l_opy_.get_data(bstack1lllllll1ll_opy_.bstack1llll111l11_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll11ll11l_opy_.get_data(bstack1lllllll1ll_opy_.bstack1lll1l1l11l_opy_, target, strict)
    @staticmethod
    def bstack11llll1lll1_opy_(target: object, strict=True):
        return bstack1lll11ll11l_opy_.get_data(bstack1lllllll1ll_opy_.bstack11lllll1111_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll11ll11l_opy_.get_data(bstack1lllllll1ll_opy_.bstack1lll1l1llll_opy_, target, strict)
    @staticmethod
    def bstack1lll11ll1l1_opy_(instance: bstack1llllll1lll_opy_) -> bool:
        return bstack1lll11ll11l_opy_.get_state(instance, bstack1lllllll1ll_opy_.bstack1lll11l1l1l_opy_, False)
    @staticmethod
    def bstack1l1lll11l11_opy_(instance: bstack1llllll1lll_opy_, default_value=None):
        return bstack1lll11ll11l_opy_.get_state(instance, bstack1lllllll1ll_opy_.bstack1lll1l1l11l_opy_, default_value)
    @staticmethod
    def bstack1l1lll1lll1_opy_(instance: bstack1llllll1lll_opy_, default_value=None):
        return bstack1lll11ll11l_opy_.get_state(instance, bstack1lllllll1ll_opy_.bstack1lll1l1llll_opy_, default_value)
    @staticmethod
    def bstack1lll11111l1_opy_(hub_url: str, bstack11lllll11l1_opy_=bstack11l111_opy_ (u"ࠥ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢᔴ")):
        try:
            bstack11llll1ll11_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll1ll11_opy_.endswith(bstack11lllll11l1_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1ll1lll11_opy_(method_name: str):
        return method_name == bstack11l111_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᔵ")
    @staticmethod
    def bstack1111111ll1_opy_(method_name: str, *args):
        return (
            bstack1lllllll1ll_opy_.bstack1l1ll1lll11_opy_(method_name)
            and bstack1lllllll1ll_opy_.bstack1llllll111l_opy_(*args) == bstack1lllllll1ll_opy_.bstack1111111lll_opy_
        )
    @staticmethod
    def bstack1l1lll11l1l_opy_(method_name: str, *args):
        if not bstack1lllllll1ll_opy_.bstack1l1ll1lll11_opy_(method_name):
            return False
        if not bstack1lllllll1ll_opy_.bstack1l1lll11lll_opy_ in bstack1lllllll1ll_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll111ll_opy_ = bstack1lllllll1ll_opy_.bstack1l1ll1lll1l_opy_(*args)
        return bstack1l1lll111ll_opy_ and bstack11l111_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᔶ") in bstack1l1lll111ll_opy_ and bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᔷ") in bstack1l1lll111ll_opy_[bstack11l111_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᔸ")]
    @staticmethod
    def bstack1l1lll1l11l_opy_(method_name: str, *args):
        if not bstack1lllllll1ll_opy_.bstack1l1ll1lll11_opy_(method_name):
            return False
        if not bstack1lllllll1ll_opy_.bstack1l1lll11lll_opy_ in bstack1lllllll1ll_opy_.bstack1llllll111l_opy_(*args):
            return False
        bstack1l1lll111ll_opy_ = bstack1lllllll1ll_opy_.bstack1l1ll1lll1l_opy_(*args)
        return (
            bstack1l1lll111ll_opy_
            and bstack11l111_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᔹ") in bstack1l1lll111ll_opy_
            and bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡣࡳ࡫ࡳࡸࠧᔺ") in bstack1l1lll111ll_opy_[bstack11l111_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᔻ")]
        )
    @staticmethod
    def bstack1llllll111l_opy_(*args):
        return str(bstack1lllllll1ll_opy_.bstack1l1llll11l1_opy_(*args)).lower()
    @staticmethod
    def bstack1l1llll11l1_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1ll1lll1l_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack111l1111l1_opy_(driver):
        command_executor = getattr(driver, bstack11l111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᔼ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack11l111_opy_ (u"ࠧࡥࡵࡳ࡮ࠥᔽ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack11l111_opy_ (u"ࠨ࡟ࡤ࡮࡬ࡩࡳࡺ࡟ࡤࡱࡱࡪ࡮࡭ࠢᔾ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack11l111_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫࡟ࡴࡧࡵࡺࡪࡸ࡟ࡢࡦࡧࡶࠧᔿ"), None)
        return hub_url
    def bstack1lllll1l1l1_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack11l111_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕀ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack11l111_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧᕁ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack11l111_opy_ (u"ࠥࡣࡺࡸ࡬ࠣᕂ")):
                setattr(command_executor, bstack11l111_opy_ (u"ࠦࡤࡻࡲ࡭ࠤᕃ"), hub_url)
                result = True
        if result:
            self.bstack1llllll1l1l_opy_ = hub_url
            bstack1lllllll1ll_opy_.bstack1lllll111ll_opy_(instance, bstack1lllllll1ll_opy_.bstack1lll1l1l11l_opy_, hub_url)
            bstack1lllllll1ll_opy_.bstack1lllll111ll_opy_(
                instance, bstack1lllllll1ll_opy_.bstack1lll11l1l1l_opy_, bstack1lllllll1ll_opy_.bstack1lll11111l1_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_]):
        return bstack11l111_opy_ (u"ࠧࡀࠢᕄ").join((bstack1lllll11111_opy_(bstack1llll1ll1ll_opy_[0]).name, bstack1llllllll1l_opy_(bstack1llll1ll1ll_opy_[1]).name))
    @staticmethod
    def bstack1llll1llll1_opy_(bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_], callback: Callable):
        bstack1l1lll1llll_opy_ = bstack1lllllll1ll_opy_.bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_)
        if not bstack1l1lll1llll_opy_ in bstack1lllllll1ll_opy_.bstack1l1111l111l_opy_:
            bstack1lllllll1ll_opy_.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_] = []
        bstack1lllllll1ll_opy_.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_].append(callback)
    def bstack1l1ll1ll1ll_opy_(self, instance: bstack1llllll1lll_opy_, method_name: str, bstack1l1lll11111_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack11l111_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᕅ")):
            return
        cmd = args[0] if method_name == bstack11l111_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᕆ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1ll1l_opy_ = bstack11l111_opy_ (u"ࠣ࠼ࠥᕇ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠼ࠥᕈ") + bstack11llll1ll1l_opy_, bstack1l1lll11111_opy_)
    def bstack1l1lll1l111_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllll1lll_opy_, str],
        bstack1llll1ll1ll_opy_: Tuple[bstack1lllll11111_opy_, bstack1llllllll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll1111_opy_, bstack1l1llll111l_opy_ = bstack1llll1ll1ll_opy_
        bstack1l1lll1llll_opy_ = bstack1lllllll1ll_opy_.bstack1l1lll11ll1_opy_(bstack1llll1ll1ll_opy_)
        self.logger.debug(bstack11l111_opy_ (u"ࠥࡳࡳࡥࡨࡰࡱ࡮࠾ࠥࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࡀࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᕉ") + str(kwargs) + bstack11l111_opy_ (u"ࠦࠧᕊ"))
        if bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.QUIT:
            if bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.PRE:
                bstack1ll11l1lll1_opy_ = bstack1lllll111l1_opy_.bstack1ll1l1l111l_opy_(EVENTS.bstack1llllll1ll_opy_.value)
                bstack1lll11ll11l_opy_.bstack1lllll111ll_opy_(instance, EVENTS.bstack1llllll1ll_opy_.value, bstack1ll11l1lll1_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠧ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࡼࡿࠣࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥ࠾ࡽࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠤᕋ").format(instance, method_name, bstack1l1llll1111_opy_, bstack1l1llll111l_opy_))
        if bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.bstack1lllll11lll_opy_:
            if bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.POST and not bstack1lllllll1ll_opy_.bstack1llll111l11_opy_ in instance.data:
                session_id = getattr(target, bstack11l111_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᕌ"), None)
                if session_id:
                    instance.data[bstack1lllllll1ll_opy_.bstack1llll111l11_opy_] = session_id
        elif (
            bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.bstack1llll1lllll_opy_
            and bstack1lllllll1ll_opy_.bstack1llllll111l_opy_(*args) == bstack1lllllll1ll_opy_.bstack1111111lll_opy_
        ):
            if bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.PRE:
                hub_url = bstack1lllllll1ll_opy_.bstack111l1111l1_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lllllll1ll_opy_.bstack1lll1l1l11l_opy_: hub_url,
                            bstack1lllllll1ll_opy_.bstack1lll11l1l1l_opy_: bstack1lllllll1ll_opy_.bstack1lll11111l1_opy_(hub_url),
                            bstack1lllllll1ll_opy_.bstack1111111l1l_opy_: int(
                                os.environ.get(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᕍ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll111ll_opy_ = bstack1lllllll1ll_opy_.bstack1l1ll1lll1l_opy_(*args)
                bstack11llll1lll1_opy_ = bstack1l1lll111ll_opy_.get(bstack11l111_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᕎ"), None) if bstack1l1lll111ll_opy_ else None
                if isinstance(bstack11llll1lll1_opy_, dict):
                    instance.data[bstack1lllllll1ll_opy_.bstack11lllll1111_opy_] = copy.deepcopy(bstack11llll1lll1_opy_)
                    instance.data[bstack1lllllll1ll_opy_.bstack1lll1l1llll_opy_] = bstack11llll1lll1_opy_
            elif bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack11l111_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣᕏ"), dict()).get(bstack11l111_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡍࡩࠨᕐ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lllllll1ll_opy_.bstack1llll111l11_opy_: framework_session_id,
                                bstack1lllllll1ll_opy_.bstack11lllll11ll_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.bstack1llll1lllll_opy_
            and bstack1lllllll1ll_opy_.bstack1llllll111l_opy_(*args) == bstack1lllllll1ll_opy_.bstack11llll1llll_opy_
            and bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.POST
        ):
            instance.data[bstack1lllllll1ll_opy_.bstack11lllll1l11_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll1llll_opy_ in bstack1lllllll1ll_opy_.bstack1l1111l111l_opy_:
            bstack1l1lll1l1ll_opy_ = None
            for callback in bstack1lllllll1ll_opy_.bstack1l1111l111l_opy_[bstack1l1lll1llll_opy_]:
                try:
                    bstack1l1lll111l1_opy_ = callback(self, target, exec, bstack1llll1ll1ll_opy_, result, *args, **kwargs)
                    if bstack1l1lll1l1ll_opy_ == None:
                        bstack1l1lll1l1ll_opy_ = bstack1l1lll111l1_opy_
                except Exception as e:
                    self.logger.error(bstack11l111_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࠤᕑ") + str(e) + bstack11l111_opy_ (u"ࠧࠨᕒ"))
                    traceback.print_exc()
            if bstack1l1llll1111_opy_ == bstack1lllll11111_opy_.QUIT:
                if bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.POST:
                    bstack1ll11l1lll1_opy_ = bstack1lll11ll11l_opy_.get_state(instance, EVENTS.bstack1llllll1ll_opy_.value)
                    if bstack1ll11l1lll1_opy_!=None:
                        bstack1lllll111l1_opy_.end(EVENTS.bstack1llllll1ll_opy_.value, bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᕓ"), bstack1ll11l1lll1_opy_+bstack11l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᕔ"), True, None)
            if bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.PRE and callable(bstack1l1lll1l1ll_opy_):
                return bstack1l1lll1l1ll_opy_
            elif bstack1l1llll111l_opy_ == bstack1llllllll1l_opy_.POST and bstack1l1lll1l1ll_opy_:
                return bstack1l1lll1l1ll_opy_
    def bstack1l1lll1ll11_opy_(
        self, method_name, previous_state: bstack1lllll11111_opy_, *args, **kwargs
    ) -> bstack1lllll11111_opy_:
        if method_name == bstack11l111_opy_ (u"ࠣࡡࡢ࡭ࡳ࡯ࡴࡠࡡࠥᕕ") or method_name == bstack11l111_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᕖ"):
            return bstack1lllll11111_opy_.bstack1lllll11lll_opy_
        if method_name == bstack11l111_opy_ (u"ࠥࡵࡺ࡯ࡴࠣᕗ"):
            return bstack1lllll11111_opy_.QUIT
        if method_name == bstack11l111_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕘ"):
            if previous_state != bstack1lllll11111_opy_.NONE:
                command_name = bstack1lllllll1ll_opy_.bstack1llllll111l_opy_(*args)
                if command_name == bstack1lllllll1ll_opy_.bstack1111111lll_opy_:
                    return bstack1lllll11111_opy_.bstack1lllll11lll_opy_
            return bstack1lllll11111_opy_.bstack1llll1lllll_opy_
        return bstack1lllll11111_opy_.NONE