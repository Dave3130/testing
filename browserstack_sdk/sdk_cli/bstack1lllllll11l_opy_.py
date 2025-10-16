# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1lllll1ll1l_opy_ import (
    bstack1lll11ll111_opy_,
    bstack1llllll11ll_opy_,
    bstack11111111ll_opy_,
    bstack1lllllll1ll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
from bstack_utils.constants import EVENTS
class bstack111111111l_opy_(bstack1lll11ll111_opy_):
    bstack1l1lll1ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠣᔲ")
    NAME = bstack1ll1ll1_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦᔳ")
    bstack1llll11ll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠥ࡬ࡺࡨ࡟ࡶࡴ࡯ࠦᔴ")
    bstack1lll1l11l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᔵ")
    bstack11lllll1l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠧ࡯࡮ࡱࡷࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᔶ")
    bstack1llll111lll_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᔷ")
    bstack1lll11l111l_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡪࡵࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡫ࡹࡧࠨᔸ")
    bstack11lllll11ll_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᔹ")
    bstack11lllll1l11_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᔺ")
    bstack1111111ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᔻ")
    bstack1lllll11ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡳ࡫ࡷࡴࡧࡶࡷ࡮ࡵ࡮ࠣᔼ")
    bstack11lllll1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠧ࡭ࡥࡵࠤᔽ")
    bstack1l11l1l1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠥᔾ")
    bstack1l1llll11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥᔿ")
    bstack1l1llll1111_opy_ = bstack1ll1ll1_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤᕀ")
    bstack11llllll111_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡴࡹ࡮ࡺࠢᕁ")
    bstack1l1111l1l11_opy_: Dict[str, List[Callable]] = dict()
    bstack1lllll11111_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lllll11l11_opy_: Any
    bstack1l1llll1ll1_opy_: Dict
    def __init__(
        self,
        bstack1lllll11111_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lllll11l11_opy_: Dict[str, Any],
        methods=[bstack1ll1ll1_opy_ (u"ࠥࡣࡤ࡯࡮ࡪࡶࡢࡣࠧᕂ"), bstack1ll1ll1_opy_ (u"ࠦࡸࡺࡡࡳࡶࡢࡷࡪࡹࡳࡪࡱࡱࠦᕃ"), bstack1ll1ll1_opy_ (u"ࠧ࡫ࡸࡦࡥࡸࡸࡪࠨᕄ"), bstack1ll1ll1_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᕅ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1lllll11111_opy_ = bstack1lllll11111_opy_
        self.platform_index = platform_index
        self.bstack1l1lll1111l_opy_(methods)
        self.bstack1lllll11l11_opy_ = bstack1lllll11l11_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack1lll11ll111_opy_.get_data(bstack111111111l_opy_.bstack1lll1l11l1l_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack1lll11ll111_opy_.get_data(bstack111111111l_opy_.bstack1llll11ll1l_opy_, target, strict)
    @staticmethod
    def bstack11lllll1ll1_opy_(target: object, strict=True):
        return bstack1lll11ll111_opy_.get_data(bstack111111111l_opy_.bstack11lllll1l1l_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack1lll11ll111_opy_.get_data(bstack111111111l_opy_.bstack1llll111lll_opy_, target, strict)
    @staticmethod
    def bstack1lll11ll1l1_opy_(instance: bstack1llllll11ll_opy_) -> bool:
        return bstack1lll11ll111_opy_.get_state(instance, bstack111111111l_opy_.bstack1lll11l111l_opy_, False)
    @staticmethod
    def bstack1l1lll1l11l_opy_(instance: bstack1llllll11ll_opy_, default_value=None):
        return bstack1lll11ll111_opy_.get_state(instance, bstack111111111l_opy_.bstack1llll11ll1l_opy_, default_value)
    @staticmethod
    def bstack1l1lll1l111_opy_(instance: bstack1llllll11ll_opy_, default_value=None):
        return bstack1lll11ll111_opy_.get_state(instance, bstack111111111l_opy_.bstack1llll111lll_opy_, default_value)
    @staticmethod
    def bstack1lll111l11l_opy_(hub_url: str, bstack11lllll111l_opy_=bstack1ll1ll1_opy_ (u"ࠢ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦᕆ")):
        try:
            bstack11lllll11l1_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11lllll11l1_opy_.endswith(bstack11lllll111l_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1l1lll11111_opy_(method_name: str):
        return method_name == bstack1ll1ll1_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕇ")
    @staticmethod
    def bstack1lllll11l1l_opy_(method_name: str, *args):
        return (
            bstack111111111l_opy_.bstack1l1lll11111_opy_(method_name)
            and bstack111111111l_opy_.bstack1llllll1111_opy_(*args) == bstack111111111l_opy_.bstack1lllll11ll1_opy_
        )
    @staticmethod
    def bstack1l1lll1ll11_opy_(method_name: str, *args):
        if not bstack111111111l_opy_.bstack1l1lll11111_opy_(method_name):
            return False
        if not bstack111111111l_opy_.bstack1l1llll11l1_opy_ in bstack111111111l_opy_.bstack1llllll1111_opy_(*args):
            return False
        bstack1l1lll111l1_opy_ = bstack111111111l_opy_.bstack1l1lll1l1ll_opy_(*args)
        return bstack1l1lll111l1_opy_ and bstack1ll1ll1_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᕈ") in bstack1l1lll111l1_opy_ and bstack1ll1ll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕉ") in bstack1l1lll111l1_opy_[bstack1ll1ll1_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᕊ")]
    @staticmethod
    def bstack1l1lll1l1l1_opy_(method_name: str, *args):
        if not bstack111111111l_opy_.bstack1l1lll11111_opy_(method_name):
            return False
        if not bstack111111111l_opy_.bstack1l1llll11l1_opy_ in bstack111111111l_opy_.bstack1llllll1111_opy_(*args):
            return False
        bstack1l1lll111l1_opy_ = bstack111111111l_opy_.bstack1l1lll1l1ll_opy_(*args)
        return (
            bstack1l1lll111l1_opy_
            and bstack1ll1ll1_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᕋ") in bstack1l1lll111l1_opy_
            and bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤᕌ") in bstack1l1lll111l1_opy_[bstack1ll1ll1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᕍ")]
        )
    @staticmethod
    def bstack1llllll1111_opy_(*args):
        return str(bstack111111111l_opy_.bstack1l1lll11lll_opy_(*args)).lower()
    @staticmethod
    def bstack1l1lll11lll_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1l1lll1l1ll_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack111ll1lll_opy_(driver):
        command_executor = getattr(driver, bstack1ll1ll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᕎ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1ll1ll1_opy_ (u"ࠤࡢࡹࡷࡲࠢᕏ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1ll1ll1_opy_ (u"ࠥࡣࡨࡲࡩࡦࡰࡷࡣࡨࡵ࡮ࡧ࡫ࡪࠦᕐ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1ll1ll1_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨࡣࡸ࡫ࡲࡷࡧࡵࡣࡦࡪࡤࡳࠤᕑ"), None)
        return hub_url
    def bstack1lllll111ll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1ll1ll1_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᕒ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1ll1ll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤᕓ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1ll1ll1_opy_ (u"ࠢࡠࡷࡵࡰࠧᕔ")):
                setattr(command_executor, bstack1ll1ll1_opy_ (u"ࠣࡡࡸࡶࡱࠨᕕ"), hub_url)
                result = True
        if result:
            self.bstack1lllll11111_opy_ = hub_url
            bstack111111111l_opy_.bstack1lllll1l1ll_opy_(instance, bstack111111111l_opy_.bstack1llll11ll1l_opy_, hub_url)
            bstack111111111l_opy_.bstack1lllll1l1ll_opy_(
                instance, bstack111111111l_opy_.bstack1lll11l111l_opy_, bstack111111111l_opy_.bstack1lll111l11l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l1lll1lll1_opy_(bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_]):
        return bstack1ll1ll1_opy_ (u"ࠤ࠽ࠦᕖ").join((bstack11111111ll_opy_(bstack1llll1l1lll_opy_[0]).name, bstack1lllllll1ll_opy_(bstack1llll1l1lll_opy_[1]).name))
    @staticmethod
    def bstack1llllll1l1l_opy_(bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_], callback: Callable):
        bstack1l1lll111ll_opy_ = bstack111111111l_opy_.bstack1l1lll1lll1_opy_(bstack1llll1l1lll_opy_)
        if not bstack1l1lll111ll_opy_ in bstack111111111l_opy_.bstack1l1111l1l11_opy_:
            bstack111111111l_opy_.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_] = []
        bstack111111111l_opy_.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_].append(callback)
    def bstack1l1lll1llll_opy_(self, instance: bstack1llllll11ll_opy_, method_name: str, bstack1l1lll11l11_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1ll1ll1_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕗ")):
            return
        cmd = args[0] if method_name == bstack1ll1ll1_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕘ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11lllll1111_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡀࠢᕙ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠢᕚ") + bstack11lllll1111_opy_, bstack1l1lll11l11_opy_)
    def bstack1l1lll11l1l_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llllll11ll_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack11111111ll_opy_, bstack1lllllll1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1l1llll1l11_opy_, bstack1l1llll11ll_opy_ = bstack1llll1l1lll_opy_
        bstack1l1lll111ll_opy_ = bstack111111111l_opy_.bstack1l1lll1lll1_opy_(bstack1llll1l1lll_opy_)
        self.logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡰࡰࡢ࡬ࡴࡵ࡫࠻ࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᕛ") + str(kwargs) + bstack1ll1ll1_opy_ (u"ࠣࠤᕜ"))
        if bstack1l1llll1l11_opy_ == bstack11111111ll_opy_.QUIT:
            if bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.PRE:
                bstack1ll111l11ll_opy_ = bstack1lllll1l11l_opy_.bstack1ll11l11l1l_opy_(EVENTS.bstack111ll1l1ll_opy_.value)
                bstack1lll11ll111_opy_.bstack1lllll1l1ll_opy_(instance, EVENTS.bstack111ll1l1ll_opy_.value, bstack1ll111l11ll_opy_)
                self.logger.debug(bstack1ll1ll1_opy_ (u"ࠤ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࡂࢁࡽࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠦࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࡀࡿࢂࠨᕝ").format(instance, method_name, bstack1l1llll1l11_opy_, bstack1l1llll11ll_opy_))
        if bstack1l1llll1l11_opy_ == bstack11111111ll_opy_.bstack1llll1lllll_opy_:
            if bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.POST and not bstack111111111l_opy_.bstack1lll1l11l1l_opy_ in instance.data:
                session_id = getattr(target, bstack1ll1ll1_opy_ (u"ࠥࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠢᕞ"), None)
                if session_id:
                    instance.data[bstack111111111l_opy_.bstack1lll1l11l1l_opy_] = session_id
        elif (
            bstack1l1llll1l11_opy_ == bstack11111111ll_opy_.bstack1llll1l1ll1_opy_
            and bstack111111111l_opy_.bstack1llllll1111_opy_(*args) == bstack111111111l_opy_.bstack1lllll11ll1_opy_
        ):
            if bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.PRE:
                hub_url = bstack111111111l_opy_.bstack111ll1lll_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack111111111l_opy_.bstack1llll11ll1l_opy_: hub_url,
                            bstack111111111l_opy_.bstack1lll11l111l_opy_: bstack111111111l_opy_.bstack1lll111l11l_opy_(hub_url),
                            bstack111111111l_opy_.bstack1111111ll1_opy_: int(
                                os.environ.get(bstack1ll1ll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠦᕟ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1l1lll111l1_opy_ = bstack111111111l_opy_.bstack1l1lll1l1ll_opy_(*args)
                bstack11lllll1ll1_opy_ = bstack1l1lll111l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᕠ"), None) if bstack1l1lll111l1_opy_ else None
                if isinstance(bstack11lllll1ll1_opy_, dict):
                    instance.data[bstack111111111l_opy_.bstack11lllll1l1l_opy_] = copy.deepcopy(bstack11lllll1ll1_opy_)
                    instance.data[bstack111111111l_opy_.bstack1llll111lll_opy_] = bstack11lllll1ll1_opy_
            elif bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1ll1ll1_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᕡ"), dict()).get(bstack1ll1ll1_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࡊࡦࠥᕢ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack111111111l_opy_.bstack1lll1l11l1l_opy_: framework_session_id,
                                bstack111111111l_opy_.bstack11lllll11ll_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1l1llll1l11_opy_ == bstack11111111ll_opy_.bstack1llll1l1ll1_opy_
            and bstack111111111l_opy_.bstack1llllll1111_opy_(*args) == bstack111111111l_opy_.bstack11llllll111_opy_
            and bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.POST
        ):
            instance.data[bstack111111111l_opy_.bstack11lllll1l11_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l1lll111ll_opy_ in bstack111111111l_opy_.bstack1l1111l1l11_opy_:
            bstack1l1lll11ll1_opy_ = None
            for callback in bstack111111111l_opy_.bstack1l1111l1l11_opy_[bstack1l1lll111ll_opy_]:
                try:
                    bstack1l1llll111l_opy_ = callback(self, target, exec, bstack1llll1l1lll_opy_, result, *args, **kwargs)
                    if bstack1l1lll11ll1_opy_ == None:
                        bstack1l1lll11ll1_opy_ = bstack1l1llll111l_opy_
                except Exception as e:
                    self.logger.error(bstack1ll1ll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨᕣ") + str(e) + bstack1ll1ll1_opy_ (u"ࠤࠥᕤ"))
                    traceback.print_exc()
            if bstack1l1llll1l11_opy_ == bstack11111111ll_opy_.QUIT:
                if bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.POST:
                    bstack1ll111l11ll_opy_ = bstack1lll11ll111_opy_.get_state(instance, EVENTS.bstack111ll1l1ll_opy_.value)
                    if bstack1ll111l11ll_opy_!=None:
                        bstack1lllll1l11l_opy_.end(EVENTS.bstack111ll1l1ll_opy_.value, bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕥ"), bstack1ll111l11ll_opy_+bstack1ll1ll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᕦ"), True, None)
            if bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.PRE and callable(bstack1l1lll11ll1_opy_):
                return bstack1l1lll11ll1_opy_
            elif bstack1l1llll11ll_opy_ == bstack1lllllll1ll_opy_.POST and bstack1l1lll11ll1_opy_:
                return bstack1l1lll11ll1_opy_
    def bstack1l1llll1l1l_opy_(
        self, method_name, previous_state: bstack11111111ll_opy_, *args, **kwargs
    ) -> bstack11111111ll_opy_:
        if method_name == bstack1ll1ll1_opy_ (u"ࠧࡥ࡟ࡪࡰ࡬ࡸࡤࡥࠢᕧ") or method_name == bstack1ll1ll1_opy_ (u"ࠨࡳࡵࡣࡵࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࠨᕨ"):
            return bstack11111111ll_opy_.bstack1llll1lllll_opy_
        if method_name == bstack1ll1ll1_opy_ (u"ࠢࡲࡷ࡬ࡸࠧᕩ"):
            return bstack11111111ll_opy_.QUIT
        if method_name == bstack1ll1ll1_opy_ (u"ࠣࡧࡻࡩࡨࡻࡴࡦࠤᕪ"):
            if previous_state != bstack11111111ll_opy_.NONE:
                command_name = bstack111111111l_opy_.bstack1llllll1111_opy_(*args)
                if command_name == bstack111111111l_opy_.bstack1lllll11ll1_opy_:
                    return bstack11111111ll_opy_.bstack1llll1lllll_opy_
            return bstack11111111ll_opy_.bstack1llll1l1ll1_opy_
        return bstack11111111ll_opy_.NONE