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
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllllll1_opy_ import (
    bstack1llll1lllll_opy_,
    bstack1llll1ll111_opy_,
    bstack1lllll11l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llllll11ll_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11l1_opy_ import bstack1llllll111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1l1lll_opy_(bstack1llllll111l_opy_):
    bstack1l1ll1l1l1l_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llllll11ll_opy_.bstack1111111l11_opy_((bstack1llll1lllll_opy_.bstack11111111l1_opy_, bstack1llll1ll111_opy_.PRE), self.bstack111111l1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack111111l1l1_opy_(
        self,
        f: bstack1llllll11ll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l1ll_opy_: Tuple[bstack1llll1lllll_opy_, bstack1llll1ll111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll111l11l_opy_(hub_url):
            if not bstack1l1ll1l1lll_opy_.bstack1l1ll1l1l1l_opy_:
                self.logger.warning(bstack111111l_opy_ (u"ࠣ࡮ࡲࡧࡦࡲࠠࡴࡧ࡯ࡪ࠲࡮ࡥࡢ࡮ࠣࡪࡱࡵࡷࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡩ࡯ࡨࡵࡥࠥࡹࡥࡴࡵ࡬ࡳࡳࡹࠠࡩࡷࡥࡣࡺࡸ࡬࠾ࠤኼ") + str(hub_url) + bstack111111l_opy_ (u"ࠤࠥኽ"))
                bstack1l1ll1l1lll_opy_.bstack1l1ll1l1l1l_opy_ = True
            return
        command_name = f.bstack1l1llll11l1_opy_(*args)
        bstack1l1lll1l11l_opy_ = f.bstack1l1lll1ll1l_opy_(*args)
        if command_name and command_name.lower() == bstack111111l_opy_ (u"ࠥࡪ࡮ࡴࡤࡦ࡮ࡨࡱࡪࡴࡴࠣኾ") and bstack1l1lll1l11l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll1l11l_opy_.get(bstack111111l_opy_ (u"ࠦࡺࡹࡩ࡯ࡩࠥ኿"), None), bstack1l1lll1l11l_opy_.get(bstack111111l_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦዀ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack111111l_opy_ (u"ࠨࡻࡤࡱࡰࡱࡦࡴࡤࡠࡰࡤࡱࡪࢃ࠺ࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡲࡶࠥࡧࡲࡨࡵ࠱ࡹࡸ࡯࡮ࡨ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡻࡧ࡬ࡶࡧࡀࠦ዁") + str(locator_value) + bstack111111l_opy_ (u"ࠢࠣዂ"))
                return
            def bstack1l1ll1l1l11_opy_(driver, bstack1l1ll1l11ll_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll1l11l1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack111111l_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࠦዃ") + str(locator_value) + bstack111111l_opy_ (u"ࠤࠥዄ"))
                    else:
                        self.logger.warning(bstack111111l_opy_ (u"ࠥࡷࡺࡩࡣࡦࡵࡶ࠱ࡳࡵ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣࡶࡪࡹࡰࡰࡰࡶࡩࡂࠨዅ") + str(response) + bstack111111l_opy_ (u"ࠦࠧ዆"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1ll11l_opy_(
                        driver, bstack1l1ll1l11ll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l1l11_opy_.__name__ = command_name
            return bstack1l1ll1l1l11_opy_
    def __1l1ll1ll11l_opy_(
        self,
        driver,
        bstack1l1ll1l11ll_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll1l11l1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack111111l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡵࡴ࡬࡫࡬࡫ࡲࡦࡦ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧ዇") + str(locator_value) + bstack111111l_opy_ (u"ࠨࠢወ"))
                bstack1l1ll1l111l_opy_ = self.bstack1l1ll11llll_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack111111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥ࡮ࡥࡢ࡮࡬ࡲ࡬ࡥࡲࡦࡵࡸࡰࡹࡃࠢዉ") + str(bstack1l1ll1l111l_opy_) + bstack111111l_opy_ (u"ࠣࠤዊ"))
                if bstack1l1ll1l111l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack111111l_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣዋ"): bstack1l1ll1l111l_opy_.locator_type,
                            bstack111111l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤዌ"): bstack1l1ll1l111l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack111111l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡎࡥࡄࡆࡄࡘࡋࠧው"), False):
                    self.logger.info(bstack1llll1ll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠭࡮࡫ࡶࡷ࡮ࡴࡧ࠻ࠢࡶࡰࡪ࡫ࡰࠩ࠵࠳࠭ࠥࡲࡥࡵࡶ࡬ࡲ࡬ࠦࡹࡰࡷࠣ࡭ࡳࡹࡰࡦࡥࡷࠤࡹ࡮ࡥࠡࡤࡵࡳࡼࡹࡥࡳࠢࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࠥࡲ࡯ࡨࡵࠥዎ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack111111l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭࡯ࡱ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠾ࠤዏ") + str(response) + bstack111111l_opy_ (u"ࠢࠣዐ"))
        except Exception as err:
            self.logger.warning(bstack111111l_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡪࡸࡲࡰࡴ࠽ࠤࠧዑ") + str(err) + bstack111111l_opy_ (u"ࠤࠥዒ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1l1ll1_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l1ll1l11l1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack111111l_opy_ (u"ࠥ࠴ࠧዓ"),
    ):
        self.bstack1llll1l1ll1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack111111l_opy_ (u"ࠦࠧዔ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack111111111l_opy_.AISelfHealStep(req)
            self.logger.info(bstack111111l_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢዕ") + str(r) + bstack111111l_opy_ (u"ࠨࠢዖ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧ዗") + str(e) + bstack111111l_opy_ (u"ࠣࠤዘ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1ll111_opy_, stage=STAGE.bstack11l11ll11_opy_)
    def bstack1l1ll11llll_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack111111l_opy_ (u"ࠤ࠳ࠦዙ")):
        self.bstack1llll1l1ll1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack111111111l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack111111l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧዚ") + str(r) + bstack111111l_opy_ (u"ࠦࠧዛ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111111l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥዜ") + str(e) + bstack111111l_opy_ (u"ࠨࠢዝ"))
            traceback.print_exc()
            raise e