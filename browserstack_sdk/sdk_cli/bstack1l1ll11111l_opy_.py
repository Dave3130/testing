# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll111ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1111_opy_,
    bstack1llll111l1l_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll111ll_opy_ import bstack1lllll1111l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1lllll1l11l_opy_ import bstack1llll111ll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1l1ll1111ll_opy_(bstack1llll111ll1_opy_):
    bstack1l1ll111lll_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lllll1111l_opy_.bstack1llll11ll11_opy_((bstack1lllllll1l1_opy_.bstack1lllll1llll_opy_, bstack1llllll1111_opy_.PRE), self.bstack1llllll1ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1llllll1ll1_opy_(
        self,
        f: bstack1lllll1111l_opy_,
        driver: object,
        exec: Tuple[bstack1llll111l1l_opy_, str],
        bstack1llll11ll1l_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1111_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll1lll111l_opy_(hub_url):
            if not bstack1l1ll1111ll_opy_.bstack1l1ll111lll_opy_:
                self.logger.warning(bstack11111_opy_ (u"ࠢ࡭ࡱࡦࡥࡱࠦࡳࡦ࡮ࡩ࠱࡭࡫ࡡ࡭ࠢࡩࡰࡴࡽࠠࡥ࡫ࡶࡥࡧࡲࡥࡥࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥ࡯࡮ࡧࡴࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣዺ") + str(hub_url) + bstack11111_opy_ (u"ࠣࠤዻ"))
                bstack1l1ll1111ll_opy_.bstack1l1ll111lll_opy_ = True
            return
        command_name = f.bstack1l1ll1lll1l_opy_(*args)
        bstack1l1ll1l11l1_opy_ = f.bstack1l1ll1ll1l1_opy_(*args)
        if command_name and command_name.lower() == bstack11111_opy_ (u"ࠤࡩ࡭ࡳࡪࡥ࡭ࡧࡰࡩࡳࡺࠢዼ") and bstack1l1ll1l11l1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1l1ll1l11l1_opy_.get(bstack11111_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤዽ"), None), bstack1l1ll1l11l1_opy_.get(bstack11111_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥዾ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack11111_opy_ (u"ࠧࢁࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࢂࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡱࡵࠤࡦࡸࡧࡴ࠰ࡸࡷ࡮ࡴࡧ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢࡲࡶࠥࡧࡲࡨࡵ࠱ࡺࡦࡲࡵࡦ࠿ࠥዿ") + str(locator_value) + bstack11111_opy_ (u"ࠨࠢጀ"))
                return
            def bstack1l1ll111l1l_opy_(driver, bstack1l1ll1111l1_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1l1ll1111l1_opy_(driver, *args, **kwargs)
                    response = self.bstack1l1ll111ll1_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack11111_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳ࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࠥጁ") + str(locator_value) + bstack11111_opy_ (u"ࠣࠤጂ"))
                    else:
                        self.logger.warning(bstack11111_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡲࡴ࠳ࡳࡤࡴ࡬ࡴࡹࡀࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࡃࡻ࡭ࡱࡦࡥࡹࡵࡲࡠࡶࡼࡴࡪࢃࠠ࡭ࡱࡦࡥࡹࡵࡲࡠࡸࡤࡰࡺ࡫࠽ࡼ࡮ࡲࡧࡦࡺ࡯ࡳࡡࡹࡥࡱࡻࡥࡾࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࡁࠧጃ") + str(response) + bstack11111_opy_ (u"ࠥࠦጄ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1l1ll111111_opy_(
                        driver, bstack1l1ll1111l1_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1l1ll111l1l_opy_.__name__ = command_name
            return bstack1l1ll111l1l_opy_
    def __1l1ll111111_opy_(
        self,
        driver,
        bstack1l1ll1111l1_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1l1ll111ll1_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack11111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡴࡳ࡫ࡪ࡫ࡪࡸࡥࡥ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࠦጅ") + str(locator_value) + bstack11111_opy_ (u"ࠧࠨጆ"))
                bstack1l1ll11l11l_opy_ = self.bstack1l1ll111l11_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack11111_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤ࡭࡫ࡡ࡭࡫ࡱ࡫ࡤࡸࡥࡴࡷ࡯ࡸࡂࠨጇ") + str(bstack1l1ll11l11l_opy_) + bstack11111_opy_ (u"ࠢࠣገ"))
                if bstack1l1ll11l11l_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack11111_opy_ (u"ࠣࡷࡶ࡭ࡳ࡭ࠢጉ"): bstack1l1ll11l11l_opy_.locator_type,
                            bstack11111_opy_ (u"ࠤࡹࡥࡱࡻࡥࠣጊ"): bstack1l1ll11l11l_opy_.locator_value,
                        }
                    )
                    return bstack1l1ll1111l1_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡍࡤࡊࡅࡃࡗࡊࠦጋ"), False):
                    self.logger.info(bstack1lll1l1l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡷࡵࡩ࠲࡮ࡥࡢ࡮࡬ࡲ࡬࠳ࡲࡦࡵࡸࡰࡹ࠳࡭ࡪࡵࡶ࡭ࡳ࡭࠺ࠡࡵ࡯ࡩࡪࡶࠨ࠴࠲ࠬࠤࡱ࡫ࡴࡵ࡫ࡱ࡫ࠥࡿ࡯ࡶࠢ࡬ࡲࡸࡶࡥࡤࡶࠣࡸ࡭࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡧࡻࡸࡪࡴࡳࡪࡱࡱࠤࡱࡵࡧࡴࠤጌ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack11111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡸࡶࡪ࠳࡮ࡰ࠯ࡶࡧࡷ࡯ࡰࡵ࠼ࠣࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡹࡿࡰࡦࡿࠣࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࢁࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠽ࠣግ") + str(response) + bstack11111_opy_ (u"ࠨࠢጎ"))
        except Exception as err:
            self.logger.warning(bstack11111_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡪࡨࡥࡱ࡯࡮ࡨ࠯ࡵࡩࡸࡻ࡬ࡵ࠼ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠦጏ") + str(err) + bstack11111_opy_ (u"ࠣࠤጐ"))
        raise exception
    @measure(event_name=EVENTS.bstack1l1ll11l1l1_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1l1ll111ll1_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack11111_opy_ (u"ࠤ࠳ࠦ጑"),
    ):
        self.bstack1llllll11l1_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack11111_opy_ (u"ࠥࠦጒ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1llll1ll1ll_opy_.AISelfHealStep(req)
            self.logger.info(bstack11111_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨጓ") + str(r) + bstack11111_opy_ (u"ࠧࠨጔ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦጕ") + str(e) + bstack11111_opy_ (u"ࠢࠣ጖"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l1ll11l111_opy_, stage=STAGE.bstack111l1l11l_opy_)
    def bstack1l1ll111l11_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack11111_opy_ (u"ࠣ࠲ࠥ጗")):
        self.bstack1llllll11l1_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1llll1ll1ll_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack11111_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦጘ") + str(r) + bstack11111_opy_ (u"ࠥࠦጙ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤጚ") + str(e) + bstack11111_opy_ (u"ࠧࠨጛ"))
            traceback.print_exc()
            raise e