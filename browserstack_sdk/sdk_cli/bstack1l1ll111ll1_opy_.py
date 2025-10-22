# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll1l1_opy_ import (
    bstack1llll1lll1l_opy_,
    bstack1lllll1l1ll_opy_,
    bstack1lllllll1l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll11l1l_opy_ import bstack1lllll11111_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1lllll11lll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll11ll1l_opy_(bstack1lllll11lll_opy_):
    bstack1l1ll11ll11_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll11111_opy_.bstack1lllllll111_opy_((bstack1llll1lll1l_opy_.bstack1llllll1lll_opy_, bstack1lllll1l1ll_opy_.PRE), self.bstack1lllll1lll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lllll1lll1_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1lll1lll_opy_(hub_url):
            if not bstack1l1ll11ll1l_opy_.bstack1l1ll11ll11_opy_:
                self.logger.warning(bstack111l1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࠥࡹࡥ࡭ࡨ࠰࡬ࡪࡧ࡬ࠡࡨ࡯ࡳࡼࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡮ࡴࡦࡳࡣࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥ࡮ࡵࡣࡡࡸࡶࡱࡃࠢዤ") + str(hub_url) + bstack111l1l_opy_ (u"ࠢࠣዥ"))
                bstack1l1ll11ll1l_opy_.bstack1l1ll11ll11_opy_ = True
            return
        command_name = f.bstack1l1ll1ll11l_opy_(*args)
        bstack1l1lll1111l_opy_ = f.bstack1l1ll1ll111_opy_(*args)
        if command_name and command_name.lower() == bstack111l1l_opy_ (u"ࠣࡨ࡬ࡲࡩ࡫࡬ࡦ࡯ࡨࡲࡹࠨዦ") and bstack1l1lll1111l_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1lll1111l_opy_.get(bstack111l1l_opy_ (u"ࠤࡸࡷ࡮ࡴࡧࠣዧ"), None), bstack1l1lll1111l_opy_.get(bstack111l1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤየ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack111l1l_opy_ (u"ࠦࢀࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࢁ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡰࡴࠣࡥࡷ࡭ࡳ࠯ࡷࡶ࡭ࡳ࡭࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡹࡥࡱࡻࡥ࠾ࠤዩ") + str(locator_value) + bstack111l1l_opy_ (u"ࠧࠨዪ"))
                return
            def bstack1l1ll111lll_opy_(driver, bstack1l1ll11l111_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll11l111_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll1111ll_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack111l1l_opy_ (u"ࠨࡳࡶࡥࡦࡩࡸࡹ࠭ࡴࡥࡵ࡭ࡵࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࠤያ") + str(locator_value) + bstack111l1l_opy_ (u"ࠢࠣዬ"))
                    else:
                        self.logger.warning(bstack111l1l_opy_ (u"ࠣࡵࡸࡧࡨ࡫ࡳࡴ࠯ࡱࡳ࠲ࡹࡣࡳ࡫ࡳࡸ࠿ࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡵࡻࡳࡩࢂࠦ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫ࡽࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࡀࠦይ") + str(response) + bstack111l1l_opy_ (u"ࠤࠥዮ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll11l1l1_opy_(
                        driver, bstack1l1ll11l111_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll111lll_opy_.__name__ = command_name
            return bstack1l1ll111lll_opy_
    def __1l1ll11l1l1_opy_(
        self,
        driver,
        bstack1l1ll11l111_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll1111ll_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack111l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡺࡲࡪࡩࡪࡩࡷ࡫ࡤ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥዯ") + str(locator_value) + bstack111l1l_opy_ (u"ࠦࠧደ"))
                bstack1l1ll111l1l_opy_ = self.bstack1l1ll11l1ll_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳ࡨࡦࡣ࡯࡭ࡳ࡭࠭ࡳࡧࡶࡹࡱࡺ࠺ࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡷࡽࡵ࡫ࡽࠡ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦࡿࠣ࡬ࡪࡧ࡬ࡪࡰࡪࡣࡷ࡫ࡳࡶ࡮ࡷࡁࠧዱ") + str(bstack1l1ll111l1l_opy_) + bstack111l1l_opy_ (u"ࠨࠢዲ"))
                if bstack1l1ll111l1l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack111l1l_opy_ (u"ࠢࡶࡵ࡬ࡲ࡬ࠨዳ"): bstack1l1ll111l1l_opy_.locator_type,
                            bstack111l1l_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࠢዴ"): bstack1l1ll111l1l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll11l111_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack111l1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡌࡣࡉࡋࡂࡖࡉࠥድ"), False):
                    self.logger.info(bstack1lll1llll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡶࡴࡨ࠱࡭࡫ࡡ࡭࡫ࡱ࡫࠲ࡸࡥࡴࡷ࡯ࡸ࠲ࡳࡩࡴࡵ࡬ࡲ࡬ࡀࠠࡴ࡮ࡨࡩࡵ࠮࠳࠱ࠫࠣࡰࡪࡺࡴࡪࡰࡪࠤࡾࡵࡵࠡ࡫ࡱࡷࡵ࡫ࡣࡵࠢࡷ࡬ࡪࠦࡢࡳࡱࡺࡷࡪࡸࠠࡦࡺࡷࡩࡳࡹࡩࡰࡰࠣࡰࡴ࡭ࡳࠣዶ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack111l1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢዷ") + str(response) + bstack111l1l_opy_ (u"ࠧࠨዸ"))
        except Exception as err:
            self.logger.warning(bstack111l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥዹ") + str(err) + bstack111l1l_opy_ (u"ࠢࠣዺ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll111l11_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1l1ll1111ll_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack111l1l_opy_ (u"ࠣ࠲ࠥዻ"),
    ):
        self.bstack1llllll11l1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack111l1l_opy_ (u"ࠤࠥዼ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll11ll11_opy_.AISelfHealStep(req)
            self.logger.info(bstack111l1l_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧዽ") + str(r) + bstack111l1l_opy_ (u"ࠦࠧዾ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠧࡸࡰࡤ࠯ࡨࡶࡷࡵࡲ࠻ࠢࠥዿ") + str(e) + bstack111l1l_opy_ (u"ࠨࠢጀ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11l11l_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def bstack1l1ll11l1ll_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack111l1l_opy_ (u"ࠢ࠱ࠤጁ")):
        self.bstack1llllll11l1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll11ll11_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack111l1l_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࠥጂ") + str(r) + bstack111l1l_opy_ (u"ࠤࠥጃ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack111l1l_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣጄ") + str(e) + bstack111l1l_opy_ (u"ࠦࠧጅ"))
            traceback.print_exc()
            raise e