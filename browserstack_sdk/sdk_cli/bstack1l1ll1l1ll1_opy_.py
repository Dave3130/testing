# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll1l111_opy_
from browserstack_sdk.sdk_cli.bstack1llllll111l_opy_ import (
    bstack1llll1l1lll_opy_,
    bstack1111111l1l_opy_,
    bstack1111111111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llll1l11ll_opy_ import bstack1llllll11l1_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll1l111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1l1111_opy_(bstack1lllll1l111_opy_):
    bstack1l1ll11llll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1llllll11l1_opy_.bstack111111l11l_opy_((bstack1llll1l1lll_opy_.bstack1llllll1111_opy_, bstack1111111l1l_opy_.PRE), self.bstack1lllll1l1l1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1l1l1_opy_(
        self,
        f: bstack1llllll11l1_opy_,
        driver: object,
        exec: Tuple[bstack1111111111_opy_, str],
        bstack11111111l1_opy_: Tuple[bstack1llll1l1lll_opy_, bstack1111111l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1lll1111ll1_opy_(hub_url):
            if not bstack1l1ll1l1111_opy_.bstack1l1ll11llll_opy_:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࠣࡷࡪࡲࡦ࠮ࡪࡨࡥࡱࠦࡦ࡭ࡱࡺࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢ࡬ࡲ࡫ࡸࡡࠡࡵࡨࡷࡸ࡯࡯࡯ࡵࠣ࡬ࡺࡨ࡟ࡶࡴ࡯ࡁࠧ኿") + str(hub_url) + bstack11l1l11_opy_ (u"ࠧࠨዀ"))
                bstack1l1ll1l1111_opy_.bstack1l1ll11llll_opy_ = True
            return
        command_name = f.bstack1l1lll11l1l_opy_(*args)
        bstack1l1lll111l1_opy_ = f.bstack1l1lll1ll11_opy_(*args)
        if command_name and command_name.lower() == bstack11l1l11_opy_ (u"ࠨࡦࡪࡰࡧࡩࡱ࡫࡭ࡦࡰࡷࠦ዁") and bstack1l1lll111l1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll111l1_opy_.get(bstack11l1l11_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨዂ"), None), bstack1l1lll111l1_opy_.get(bstack11l1l11_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢዃ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠤࡾࡧࡴࡳ࡭ࡢࡰࡧࡣࡳࡧ࡭ࡦࡿ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡵࡲࠡࡣࡵ࡫ࡸ࠴ࡵࡴ࡫ࡱ࡫ࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡯ࡳࠢࡤࡶ࡬ࡹ࠮ࡷࡣ࡯ࡹࡪࡃࠢዄ") + str(locator_value) + bstack11l1l11_opy_ (u"ࠥࠦዅ"))
                return
            def bstack1l1ll1l111l_opy_(driver, bstack1l1ll1l11ll_opy_, *args, **kwargs):
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
                        self.logger.info(bstack11l1l11_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࠢ዆") + str(locator_value) + bstack11l1l11_opy_ (u"ࠧࠨ዇"))
                    else:
                        self.logger.warning(bstack11l1l11_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭࡯ࡱ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠾ࠤወ") + str(response) + bstack11l1l11_opy_ (u"ࠢࠣዉ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll1l1lll_opy_(
                        driver, bstack1l1ll1l11ll_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll1l111l_opy_.__name__ = command_name
            return bstack1l1ll1l111l_opy_
    def __1l1ll1l1lll_opy_(
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
                self.logger.info(bstack11l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡸࡷ࡯ࡧࡨࡧࡵࡩࡩࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࠣዊ") + str(locator_value) + bstack11l1l11_opy_ (u"ࠤࠥዋ"))
                bstack1l1ll1ll11l_opy_ = self.bstack1l1ll1l1l1l_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡪࡨࡥࡱ࡯࡮ࡨࡡࡵࡩࡸࡻ࡬ࡵ࠿ࠥዌ") + str(bstack1l1ll1ll11l_opy_) + bstack11l1l11_opy_ (u"ࠦࠧው"))
                if bstack1l1ll1ll11l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11l1l11_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦዎ"): bstack1l1ll1ll11l_opy_.locator_type,
                            bstack11l1l11_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧዏ"): bstack1l1ll1ll11l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1l11ll_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11l1l11_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡊࡡࡇࡉࡇ࡛ࡇࠣዐ"), False):
                    self.logger.info(bstack1llll1111_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠰ࡱ࡮ࡹࡳࡪࡰࡪ࠾ࠥࡹ࡬ࡦࡧࡳࠬ࠸࠶ࠩࠡ࡮ࡨࡸࡹ࡯࡮ࡨࠢࡼࡳࡺࠦࡩ࡯ࡵࡳࡩࡨࡺࠠࡵࡪࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࠡ࡮ࡲ࡫ࡸࠨዑ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11l1l11_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰ࡲࡴ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࡁࠧዒ") + str(response) + bstack11l1l11_opy_ (u"ࠥࠦዓ"))
        except Exception as err:
            self.logger.warning(bstack11l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹࡀࠠࡦࡴࡵࡳࡷࡀࠠࠣዔ") + str(err) + bstack11l1l11_opy_ (u"ࠧࠨዕ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll1ll111_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1l1ll1l11l1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11l1l11_opy_ (u"ࠨ࠰ࠣዖ"),
    ):
        self.bstack1llllllll11_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11l1l11_opy_ (u"ࠢࠣ዗")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1ll11l_opy_.AISelfHealStep(req)
            self.logger.info(bstack11l1l11_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥዘ") + str(r) + bstack11l1l11_opy_ (u"ࠤࠥዙ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣዚ") + str(e) + bstack11l1l11_opy_ (u"ࠦࠧዛ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll1l1l11_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1l1ll1l1l1l_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11l1l11_opy_ (u"ࠧ࠶ࠢዜ")):
        self.bstack1llllllll11_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1ll11l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11l1l11_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣዝ") + str(r) + bstack11l1l11_opy_ (u"ࠢࠣዞ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨዟ") + str(e) + bstack11l1l11_opy_ (u"ࠤࠥዠ"))
            traceback.print_exc()
            raise e